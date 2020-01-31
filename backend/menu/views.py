import json

from django.shortcuts import render

from django.db.models import Sum, F

from menu.models import Menu, DishOrder
from dish.models import Dish

from menu.serializers import MenuSerializer
from dish.serializers import DishMenuSerializer

from calorie.api import APIView
from calorie.api import get_user_id

# Create your views here.


class GetMenuHistoryAPI(APIView):
    def get(self, request):
        try:
            user_id = get_user_id(request)
            user_menu_objects = Menu.objects.filter(user_id=user_id, if_show=True)
            menu_ids = user_menu_objects.values_list('id', flat=True)
            calories = DishOrder.objects.filter(menu__in=menu_ids).values('menu_id').\
                annotate(calorie=Sum(F('mass') * F('dish__calorie'))).values('menu_id', 'calorie')
            user_menus = MenuSerializer(user_menu_objects, many=True).data[:10]
            for menu in user_menus:
                menu['calorie'] = list(filter(lambda x: x['menu_id'] == menu['id'], calories))[0]['calorie']
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'user_menus': user_menus})


class SubmitMenuAPI(APIView):
    def post(self, request):
        try:
            json_data = json.loads(request.body)
            user_id = get_user_id(request)
            menu_object = Menu.objects.create(if_show=True, user_id=user_id)
            menu_object.save()
            dishes = json_data['dishes']
            for dish in dishes:
                dishorder_object = DishOrder.objects.create(dish__id=dish['dish_id'], mass=dish['mass'], menu=menu_object)
                dishorder_object.save()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()


class MenuDetailAPI(APIView):
    def get(self, request):
        request_data = request.query_params
        try:
            menu_id = request_data['menu_id']
            dishorder_objects = DishOrder.objects.filter(menu=menu_id)
            dish_ids = dishorder_objects.values_list('dish', flat=True)
            dish_infos = dishorder_objects.values('dish', 'mass')
            dish_objects = Dish.objects.filter(id__in=dish_ids).all()
            dishes = DishMenuSerializer(dish_objects, many=True).data
            for dish in dishes:
                dish['mass'] = list(filter(lambda x: x['dish'] == dish['id'], dish_infos))[0]['mass']
                dish['calorie'] = dish['mass'] * dish['calorie']
        except Exception as e:
            return self.error(err=str(e))
        return self.success(data={'dishes': dishes})


class DeleteMenuAPI(APIView):
    def post(self, request):
        try:
            json_data = json.loads(request.body)
            user_id = get_user_id(request)
            menu_id = json_data['menu_id']
            menu_object = Menu.objects.get(pk=menu_id)
            menu_object.delete()
        except Exception as e:
            return self.error(err=str(e))
        return self.success()
