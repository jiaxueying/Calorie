"""
administrate.urls
"""
# views is used to log in
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.Test.as_view()),
]
