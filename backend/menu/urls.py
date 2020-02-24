"""
menu.url
"""

from django.urls import path
from menu.views import GetMenuHistoryAPI, SubmitMenuAPI, MenuDetailAPI, DeleteMenuAPI

urlpatterns = [
    path('query/', GetMenuHistoryAPI.as_view()),
    path('order/', SubmitMenuAPI.as_view()),
    path('detail/', MenuDetailAPI.as_view()),
    path('delete/', DeleteMenuAPI.as_view()),
]
