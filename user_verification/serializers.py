# user_verification/serializers.py
from rest_framework import serializers

class PhoneNumberVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
