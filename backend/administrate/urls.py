"""
administrate.urls
"""
# views is used to log in
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.Test.as_view()),
    path('login/', views.Login.as_view()),
    path('ingredient/add/', views.AddIngredient.as_view()),
    path('ingredient/edit/', views.EditIngredient.as_view()),
    path('ingredient/delete/', views.DeleteIngredient.as_view()),
    path('ingredient/get/', views.GetIngredient.as_view()),
    path('ingredient/all/', views.AllIngredient.as_view()),
    path('dish/add/', views.AddDish.as_view()),
    path('dish/edit/', views.EditDish.as_view()),
    path('dish/delete/', views.DeleteDish.as_view()),
]
