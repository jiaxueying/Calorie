"""
dish.views
"""

import json

from django.db import transaction
from calorie.api import APIView
from calorie.api import check_and_get_str, check_and_get_int, check_one_field, FieldException
from dish.models import Dish
from dish.serializers import DishSerializer
from dish.serializers import DishWithLikeSerializer
from dish.query import DishQueryFunctionSet
from user.models import LikeDish
from dish.api import recommend

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
        offset = check_and_get_int(request.query_params, "offset")
        limit = check_and_get_int(request.query_params, "limit")
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
            return self.success(data=serializer.data[offset:offset+limit])
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
        offset = check_and_get_int(request.query_params, "offset")
        limit = check_and_get_int(request.query_params, "limit")
        dishes = DishQueryFunctionSet.keyword(request.user, keyword)
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data[offset:offset+limit])
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
        offset = check_and_get_int(request.query_params, "offset")
        limit = check_and_get_int(request.query_params, "limit")
        dishes = DishQueryFunctionSet.calorie(
            request.user, min_calorie, max_calorie)
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data[offset:offset+limit])
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
            dish_object.views += 1
            dish_object.save()
            dish = DishSerializer(dish_object).data

            equ = {
                "圣女果": [0, 10],
                "薯片": [10, 20],
                "饼干": [20, 30],
                "西瓜": [30, 50],
                "冰淇淋": [50, 60],
                "巧克力": [60, 90],
                "烤肠": [90, 120],
                "烤鸡翅": [120, 200],
                "可乐": [200, 250],
                "蛋糕": [250, 280],
                "炸鸡腿": [280, 320],
                "薯条": [320, 450],
                "披萨": [450, 500],
                "汉堡": [500, float('inf')],
            }

            ener = dish["calorie"]
            for name, range_ in equ.items():
                if range_[0] < ener <= range_[1]:
                    dish["equivalent"] = "/media/static/icon/" + name + ".png"
                    break

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
            likedish_object, _ = LikeDish.objects.get_or_create(
                dish_id=dish_id, user=user)
            with transaction.atomic():
                if likedish_object.like is not None:
                    if likedish_object.like:
                        dish_object.like -= 1
                    else:
                        dish_object.dislike -= 1

                if str(like) == "1" and str(dislike) == "0":
                    likedish_object.like = True
                    dish_object.like += 1
                elif str(like) == "0" and str(dislike) == "1":
                    likedish_object.like = False
                    dish_object.dislike += 1
                elif str(like) == "0" and str(dislike) == "0":
                    likedish_object.like = None
                else:
                    raise FieldException("点赞和点踩的值应该是bool类型，并且不能全为1")
                likedish_object.save()
                dish_object.save()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()


class Recommend(APIView):
    '''推荐菜品'''

    def get(self, request):
        '''get方法'''
        try:
            dishes = recommend()
            return self.success(data=dishes)
        except Exception as e:
            return self.error(err=str(e))
