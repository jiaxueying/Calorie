"""
dish.views
"""

import json

from django.db.models import F, FilteredRelation, Q
from django.db import transaction
from calorie.api import APIView
from calorie.api import check_and_get_str, check_and_get_int, check_one_field, FieldException
from dish.models import Dish
from dish.serializers import DishSerializer
from dish.serializers import DishWithLikeSerializer
from dish.query import DishQueryFunctionSet
from dish.models import Dish, Tag
from user.models import LikeDish

# Create your views here.


class TagQueryAPI(APIView):
    """
    通过标签查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        check_one_field(request.query_params, "tag_id")
        tag_ids = request.query_params['tag_id']
        if not tag_ids:
            return FieldException("tag_id不能为空")
        if tag_ids[0] != "[":
            tag_ids = check_and_get_int(request.query_params, "tag_id")
            tag_ids = [tag_ids]
        else:
            tag_ids = json.loads(tag_ids)
        dishes = DishQueryFunctionSet.tag_ids(request.user, tag_ids)
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data)
        except Exception as e:
            return self.error(err=str(e))


class KeyQueryAPI(APIView):
    """
    通过关键词查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        keyword = check_and_get_str(request.query_params, 'key_word')
        dishes = DishQueryFunctionSet.keyword(request.user, keyword)
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data)
        except Exception as e:
            return self.error(err=str(e))


class CalorieQueryAPI(APIView):
    """
    通过卡路里的上下限查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        min_calorie = check_and_get_int(request.query_params, "min_calorie")
        max_calorie = check_and_get_int(request.query_params, "max_calorie")
        dishes = DishQueryFunctionSet.calorie(request.user, min_calorie, max_calorie)
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data)
        except Exception as e:
            return self.error(err=str(e))

class DishDetailAPI(APIView):
    """
    获取菜品详情
    """
    def get(self, request):
        """
        get方法
        """
        request_data = request.query_params
        try:
            dish_id = request_data['dish_id']
            dish_object = Dish.objects.get(id=dish_id)
            dish = DishSerializer(dish_object).data
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'dish': dish})


class LikeDishAPI(APIView):
    """
    赞/踩菜品
    """
    def post(self, request):
        """
        post方法
        """
        try:
            user = request.user
            dish_id = request.data['dish_id']
            like = request.data['like']
            dislike = request.data['dislike']
            dish_object = Dish.objects.get(pk=dish_id)

            likedish_object, _ = LikeDish.objects.get_or_create(dish_id=dish_id, user=user)
            with transaction.atomic():

                if likedish_object.like is not None:
                    if likedish_object.like:
                        dish_object.like -= 1
                    else:
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
                    raise FieldException("点赞和点踩的值应该是bool类型，并且不能全为1")

                likedish_object.save()
                dish_object.save()

        except Exception as e:
            return self.error(err=str(e))
        return self.success()
