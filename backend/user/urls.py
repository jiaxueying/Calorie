"""
user.urls
"""
# views is used to log in
from django.urls import path

from user.views import UserLoginAPI
from user.views import UserProfileAPI

urlpatterns = [
    path('login/', UserLoginAPI.as_view()),
    path('profile/', UserProfileAPI.as_view()),
]
