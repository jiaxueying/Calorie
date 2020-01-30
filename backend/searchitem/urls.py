from django.urls import path
# views is used to log in
from rest_framework.authtoken import views

from searchitem.views import GetSearchHistoryAPI

urlpatterns = [
    path('query/', GetSearchHistoryAPI.as_view()),
]
