from django.urls import path
# views is used to log in
from rest_framework.authtoken import views

from user.views import UserLoginAPI

urlpatterns = [
    path('login/', UserLoginAPI.as_view()),
]
