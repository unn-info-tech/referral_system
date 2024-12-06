from django.shortcuts import render
from django.http import Http404
from .utils import generate_verification_code
from rest_framework.views import APIView
from rest_framework.response import Response
#from twilio.rest import Client
from .serializers import PhoneNumberVerificationSerializer
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from .models import CustomUser, InviteCode
import time
import random
import string
from rest_framework import status


class PhoneNumberVerificationView(APIView):
    def get(self, request):
        return render(request, 'user_verification/verification_form.html')
    
    def post(self, request):
        serializer = PhoneNumberVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = generate_verification_code()
            print(verification_code)

            '''# Initialize Twilio client
            account_sid = 'ACb38e675436f00fcc6047c52b21cd4a38'
            auth_token = '55fde810186a6bdedc810933ea835b66'
            client = Client(account_sid, auth_token)

            # Send SMS
            message = client.messages.create(
                body=f"Your verification code is: {verification_code}",
                from_='+19403503116',
                to=phone_number
            )'''
            

            request.session['verification_code'] = verification_code
            request.session['phone_number'] = phone_number

            time.sleep(2)  

            return redirect('verify-code')
        else:
            return render(request, 'user_verification/error.html', {'error': 'Ввод недействителен'})



class CodeVerificationView(APIView):
    def get(self, request):
        return render(request, 'user_verification/verify_code.html', {"OTP": request.session.get('verification_code')})

    def post(self, request):
        entered_code = request.data.get('user_code')  
        stored_code = request.session.get('verification_code')

        if entered_code == stored_code:
            print("Phone number from session:", request.session.get('phone_number'))

            phone_number = request.session.get('phone_number')
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                user = CustomUser(phone_number=phone_number)
                user.save()

                invite_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
                invite = InviteCode(invite_code=invite_code)
                invite.save()
 
                user.my_invite_code = invite
                user.is_verified = True
                user.save()


            del request.session['verification_code']
            return redirect('my-page')
        else:
            return render(request, 'user_verification/verify_code.html', {'error_message': 'Invalid code'})
        


class MyPageView(APIView):
    def get(self, request):
        phone_number = request.session.get('phone_number')
        
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return render(request, 'user_verification/error.html', {'error': 'Пользователь не найден'})
        
        if user.is_verified:
            friends = CustomUser.objects.filter(friend_invite_code=user.my_invite_code)
            
            context = {
                'user': user,
                'friends': friends
            }
            
            return render(request, 'user_verification/my_page.html', context)
        else:
            return render(request, 'user_verification/error.html', {'error': 'Пользователь не проверен'})
        

    
class VerifyFriendInviteView(APIView):
    def post(self, request):
        phone_number = request.session.get('phone_number')
        
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return render(request, 'user_verification/error.html', {'error': 'Пользователь не найден'})
        
        if user.is_verified:
            friend_invite_code = request.POST.get('friend_invite_code')
            
            try:
                invite = InviteCode.objects.get(invite_code=friend_invite_code)
            except InviteCode.DoesNotExist:
                return render(request, 'user_verification/error.html', {'error': 'Неверный код приглашения друга'})
            
            user.friend_invite_code = invite
            user.save()
            
            return redirect('my-page') 
        else:
            return render(request, 'user_verification/error.html', {'error': 'Пользователь не проверен'})







