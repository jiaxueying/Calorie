"""
menu.views
"""

import json

from django.db.models import Sum, F

from menu.models import Menu, DishOrder
from menu.serializers import MenuSerializer

from dish.models import Dish
from dish.serializers import DishMenuSerializer

from calorie.api import APIView
from calorie.api import get_user_id,check_and_get_int

# Create your views here.


class GetMenuHistoryAPI(APIView):
    """
    查询历史菜单
    """

    def get(self, request):
        """
        get方法
        """
        try:
            user_id = get_user_id(request)
            offset = check_and_get_int(request.query_params, "offset")
            limit = check_and_get_int(request.query_params, "limit")
            user_menu_objects = Menu.objects.filter(
                user_id=user_id, if_show=True)
            menu_ids = user_menu_objects.values_list('id', flat=True)
            calories = DishOrder.objects.filter(menu__in=menu_ids).values('menu_id').\
                annotate(calorie=Sum(F('mass') * F('dish__calorie'))
                         ).values('menu_id', 'calorie')
            user_menus = MenuSerializer(user_menu_objects, many=True).data[offset:offset+limit]
            for menu in user_menus:
                menucal = list(
                    filter(lambda x: x['menu_id'] == menu['id'], calories))
                if not menucal:
                    Menu.objects.get(id=menu['id']).delete()
                    menu['id'] = -1
                else:
                    menu['calorie'] = menucal[0]['calorie']
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'user_menus': filter(lambda x: x['id'] != -1, user_menus)})


class SubmitMenuAPI(APIView):
    """
    提交菜单
    """

    def post(self, request):
        """
        post方法
        """
        try:
            json_data = request.data
            user_id = get_user_id(request)
            menu_object = Menu.objects.create(if_show=True, user_id=user_id)
            menu_object.save()
            dishes = json.loads(json_data['dishes'])
            for dish in dishes:
                dishorder_object = DishOrder.objects.create(
                    dish_id=dish['dish_id'], mass=dish['mass'], menu=menu_object)
                dishorder_object.save()
                dish_object = Dish.objects.get(id=dish["dish_id"])
                dish_object.orders += 1
                dish_object.save()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()


class MenuDetailAPI(APIView):
    """
    查看菜单详情
    """

    def get(self, request):
        """
        get方法
        """
        request_data = request.query_params
        try:
            menu_id = request_data['menu_id']
            dishorder_objects = DishOrder.objects.filter(menu=menu_id)
            dish_ids = dishorder_objects.values_list('dish', flat=True)
            dish_infos = dishorder_objects.values('dish', 'mass')
            dish_objects = Dish.objects.filter(id__in=dish_ids).all()
            dishes = DishMenuSerializer(dish_objects, many=True).data
            for dish in dishes:
                dish['mass'] = list(filter(lambda x: x['dish'] == dish['id'], dish_infos))[
                    0]['mass']
                dish['calorie'] = dish['mass'] * dish['calorie']
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'dishes': dishes})


class DeleteMenuAPI(APIView):
    """
    删除菜单
    可以在后期考虑使用delete方法
    """

    def post(self, request):
        """
        post方法
        """
        try:
            json_data = json.loads(request.body)
            menu_id = json_data['menu_id']
            menu_object = Menu.objects.get(pk=menu_id)
            menu_object.delete()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()
