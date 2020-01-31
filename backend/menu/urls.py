from django.urls import path
# views is used to log in
from rest_framework.authtoken import views

from menu.views import GetMenuHistoryAPI, SubmitMenuAPI, MenuDetailAPI, DeleteMenuAPI

urlpatterns = [
    path('query/', GetMenuHistoryAPI.as_view()),
    path('submit/', SubmitMenuAPI.as_view()),
    path('detail/', MenuDetailAPI.as_view()),
    path('delete/', DeleteMenuAPI.as_view()),
]
