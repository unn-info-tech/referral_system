# user_verification/urls.py
from django.urls import path
from .views import PhoneNumberVerificationView
from .views import CodeVerificationView


urlpatterns = [
    path('verify-phone/', PhoneNumberVerificationView.as_view(), name='verify-phone'),
    path('verify-code/', CodeVerificationView.as_view(), name='verify-code'),
]
