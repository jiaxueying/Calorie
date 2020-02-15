"""
dish.views
"""
# TODO
# 1. 序列化器更改
# 2. 图片文件的存储目录
# 3. 关于get_user_like函数数据库查询优化
# 4. 为达成接口标准的接口修改

import json
from django.db.models import F, FilteredRelation, Q
from calorie.api import APIView
from calorie.api import get_user_id, check_and_get_str, check_and_get_int
from dish.models import Dish, Tag
from dish.serializers import DishSerializer
from dish.serializers import DishWithLikeSerializer

from user.models import LikeDish

# Create your views here.

# deprecated
def get_user_like(dishes, user_id):
    """
    查询用户是否喜欢该菜品
    """
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
    """
    通过标签查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        tag_id = check_and_get_int(request.query_params, "tag_id")
        dishes = Tag.objects.get(pk=tag_id).dish_set.annotate(
            t=FilteredRelation('likedish', condition=Q(likedish__user_id=request.user.id))
        ).annotate(user_like=F('t__like')).annotate(user_dislike=1-F('t__like'))
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data)
        except Exception as e:
            print(e)
            return self.error(err=str(e))



# How to execute like the following raw sql
# select a.name as dish_name, b.like as user_like from dish_dish a left join (select * from user_likedish where user_id=1) b on a.id = b.dish_id where a.name like "肉丝";
class KeyQueryAPI(APIView):
    """
    通过关键词查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        key_word = check_and_get_str(request.query_params, 'key_word')
        dishes = Dish.objects.filter(name__contains=key_word).annotate(
            t=FilteredRelation('likedish', condition=Q(likedish__user_id=request.user.id))
        ).annotate(user_like=F('t__like')).annotate(user_dislike=1-F('t__like'))
        serializer = DishWithLikeSerializer(dishes, many=True)
        try:
            return self.success(data=serializer.data)
        except Exception as e:
            print(e)
            return self.error(err=str(e))


class CalorieQueryAPI(APIView):
    """
    通过卡路里的上下限查询菜品
    """
    def get(self, request):
        """
        get 方法
        """
        print(request.user.id)
        min_calorie = check_and_get_int(request.query_params, "min_calorie")
        max_calorie = check_and_get_int(request.query_params, "max_calorie")
        dishes = Dish.objects.filter(
            calorie__gt=min_calorie, calorie__lt=max_calorie).annotate(
                t=FilteredRelation('likedish', condition=Q(likedish__user_id=request.user.id))
            ).annotate(user_like=F('t__like')).annotate(user_dislike=1-F('t__like'))
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
            json_data = request.data
            user_id = get_user_id(request)
            dish_id = json_data['dish_id']
            like = json_data['like']
            dislike = json_data['dislike']
            likedish_object = LikeDish.objects.filter(dish_id=dish_id, user_id=user_id).first()
            dish_object = Dish.objects.get(pk=dish_id)
            if not likedish_object:
                likedish_object = LikeDish.objects.create(dish_id=dish_id, user_id=user_id)
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
