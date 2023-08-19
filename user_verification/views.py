from django.shortcuts import render
from .utils import generate_verification_code
from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from .serializers import PhoneNumberVerificationSerializer
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from .models import CustomUser, InviteCode
import time
import random
import string


class PhoneNumberVerificationView(APIView):
    def get(self, request):
        return render(request, 'user_verification/verification_form.html')
    
    def post(self, request):
        serializer = PhoneNumberVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = generate_verification_code()

            # Initialize Twilio client
            account_sid = 'AC82d051a0657600868f58f6ede62f1754'
            auth_token = '900598d015e04cad5b581b0262911b1f'
            client = Client(account_sid, auth_token)

            # Send SMS
            message = client.messages.create(
                body=f"Your verification code is: {verification_code}",
                from_='+16184861853',
                to=phone_number
            )

            # Store the verification code in the session for later validation
            request.session['verification_code'] = verification_code
            request.session['phone_number'] = phone_number

            time.sleep(2)  # Introduce a 2-second delay

            return redirect('verify-code')
        else:
            return self.response_for_error(request)



class CodeVerificationView(APIView):
    def get(self, request):
        # Display the verification code entry form
        return render(request, 'user_verification/verify_code.html')

    def post(self, request):
        entered_code = request.data.get('user_code')  # Assuming you're using POST data
        stored_code = request.session.get('verification_code')

        if entered_code == stored_code:
            # Code is correct, perform desired actions
            # ...
            print("Phone number from session:", request.session.get('phone_number'))

            phone_number = request.session.get('phone_number')
            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                # If user is not registered, create a new user
                user = CustomUser(phone_number=phone_number)
                user.save()

                # Generate a random 6-digit invite code
                invite_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
                invite = InviteCode(invite_code=invite_code)
                invite.save()
 
                # Now set the invite code to the user's my_invite_code field
                user.my_invite_code = invite
                user.save()


            del request.session['verification_code']
            return Response({"message": "Verification successful. You can proceed with registration."})
            #return render(request, 'user_verification/verify_success.html')
        else:
            # Code is incorrect, display error message
            return render(request, 'user_verification/verify_code.html', {'error_message': 'Invalid code'})






