import json

from django.shortcuts import render

from dish.models import Dish
from user.models import LikeDish

from dish.serializers import DishSerializer

from calorie.api import APIView
from calorie.api import get_user_id

# Create your views here.


def get_user_like(dishes, user_id):
    for dish in dishes:
        dish['user_like'] = 0
        dish['user_dislike'] = 0
        likedish_object = LikeDish.objects.filter(dish__id=dish['id'], user__id=user_id).first()
        if likedish_object:
            if likedish_object.like == True:
                dish['user_like'] = 1
            elif likedish_object.like == False:
                dish['user_dislike'] = 1


class TagQueryAPI(APIView):
    pass


class KeyQueryAPI(APIView):
    pass


class CalorieQueryAPI(APIView):
    def get(self, request):
        request_data = request.query_params
        try:
            user_id = get_user_id(request)
            min_calorie = int(request_data['min_calorie'])
            max_calorie = int(request_data['max_calorie'])
            dish_objects = Dish.objects.filter(calorie__gt=min_calorie, calorie__lt=max_calorie)
            dishes = DishSerializer(dish_objects, many=True).data
            get_user_like(dishes, user_id)
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'dishes': dishes})


class DishDetailAPI(APIView):
    def get(self, request):
        request_data = request.query_params
        try:
            dish_id = request_data['dish_id']
            dish_object = Dish.objects.get(id=dish_id)
            dish = DishSerializer(dish_object).data
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'dish': dish})


class LikeDishAPI(APIView):
    def post(self, request):
        try:
            json_data = json.loads(request.body)
            user_id = get_user_id(request)
            dish_id = json_data['dish_id']
            like = json_data['like']
            dislike = json_data['dislike']
            likedish_object = LikeDish.objects.filter(dish__id=dish_id, user__id=user_id).first()
            dish_object = Dish.objects.get(pk=dish_id)
            if not likedish_object:
                likedish_object = LikeDish.objects.create(dish__id=dish_id, user__id=user_id)
            else:
                if likedish_object.like == True:
                    dish_object.like -= 1
                elif likedish_object.like == False:
                    dish_object.dislike -= 1
            if like == "1" and dislike == "0":
                likedish_object.like = True
                dish_object.like += 1
            elif like == "0" and dislike == "1":
                likedish_object.like = False
                dish_object.dislike += 1
            elif like == "0" and dislike == "0":
                likedish_object.like = None
            else:
                raise Exception("Like/Dislike Status Error")
            likedish_object.save()
            dish_object.save()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()
