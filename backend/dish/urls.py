from django.urls import path
# views is used to log in
from rest_framework.authtoken import views

from dish.views import TagQueryAPI, KeyQueryAPI, CalorieQueryAPI, DishDetailAPI, LikeDishAPI

urlpatterns = [
    path('tag_query/', TagQueryAPI.as_view()),
    path('key_query/', KeyQueryAPI.as_view()),
    path('calorie_query/', CalorieQueryAPI.as_view()),
    path('detail/', DishDetailAPI.as_view()),
    path('like/', LikeDishAPI.as_view()),
]
