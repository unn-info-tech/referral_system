'''# LOGIN
@api_view(['POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = CustomUser.objects.filter(email=email).first()
        if user:
            # Check user's password
            if user.check_password(password):
                # Authenticate user
                auth_user = authenticate(username=user.email, password=password)
                if auth_user:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''