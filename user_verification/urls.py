# user_verification/urls.py
from django.urls import path
from .views import PhoneNumberVerificationView
from .views import CodeVerificationView
from .views import MyPageView
from .views import VerifyFriendInviteView





urlpatterns = [
    path('verify-phone/', PhoneNumberVerificationView.as_view(), name='verify-phone'),
    path('verify-code/', CodeVerificationView.as_view(), name='verify-code'),
    path('my-page/', MyPageView.as_view(), name='my-page'),
    path('verify-friend-invite/', VerifyFriendInviteView.as_view(), name='verify-friend-invite'),
    
]
