"""
admin.views
"""
import json
from calorie.api import APIView, check_and_get_str, check_one_field
from administrate.api import APIviewPlus, AuthToken, get_dish_data
from administrate.models import Auth, Nutrition
from administrate.serializers import IngredientSerializer, OnlyNameIngredientSerializer
from dish.serializers import DishSerializer
from dish.models import Dish


class Test(APIviewPlus):
    '''
    测试
    '''

    def get_plus(self, request):
        return self.success()


class Login(APIView):
    '''登录'''

    def post(self, request):
        '''post方法'''

        account = check_and_get_str(request.data, "account")
        password = check_and_get_str(request.data, "password")
        admin = Auth.objects.filter(account=account, password=password)
        if not admin:
            return self.error(err="账号或密码错误")
        else:
            token = AuthToken.update_token(admin[0].id)
            return self.success(data={"token": token})


class AddIngredient(APIviewPlus):
    '''添加一项食材数据'''

    def post_plus(self, request):
        try:
            ingredient_obj = IngredientSerializer(data=request.data)
            if ingredient_obj.is_valid(raise_exception=True):
                ingredient_obj.save()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))


class EditIngredient(APIviewPlus):
    '''修改营养成分表中的数据'''

    def post_plus(self, request):
        nutrition_id = check_and_get_str(request.data, "id")
        try:
            obj = Nutrition.objects.get(id=nutrition_id)
            ingredient_obj = IngredientSerializer(
                instance=obj, data=request.data)
            if ingredient_obj.is_valid(raise_exception=True):
                ingredient_obj.save()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))


class DeleteIngredient(APIviewPlus):
    '''删除一条营养成分表中的数据'''

    def get_plus(self, request):
        nutrition_id = check_and_get_str(request.query_params, "id")
        try:
            obj = Nutrition.objects.get(id=nutrition_id)
            obj.delete()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))


class GetIngredient(APIviewPlus):
    '''查看营养成分表中的某一条数据'''

    def get_plus(self, request):
        nutrition_id = check_and_get_str(request.query_params, "id")
        try:
            obj = Nutrition.objects.get(id=nutrition_id)
            data = IngredientSerializer(obj).data
            return self.success(data=data)
        except Exception as e:
            return self.error(err=str(e))


class AllIngredient(APIviewPlus):
    '''获取所有食材'''

    def get_plus(self, request):
        try:
            data = OnlyNameIngredientSerializer(
                Nutrition.objects.all(), many=True).data
            return self.success(data=data)
        except Exception as e:
            return self.error(err=str(e))


class AddDish(APIviewPlus):
    '''添加菜品'''

    def post_plus(self, request):
        raw_data = {}
        raw_data['name'] = check_and_get_str(request.data, "name")
        check_one_field(request.FILES, "picture")
        raw_data["picture"] = request.FILES["picture"]
        check_one_field(request.data, "ingredient")
        try:
            raw_data["ingredient"] = json.loads(request.data["ingredient"])
            dish_data = get_dish_data(raw_data)
            dish_obj = DishSerializer(data=dish_data)
            if dish_obj.is_valid(raise_exception=True):
                dish_obj.save()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))


class EditDish(APIviewPlus):
    '''修改菜品'''

    def post_plus(self, request):
        raw_data = {}
        try:
            raw_data['picture'] = request.FILES['picture']
        except Exception:
            pass

        raw_data['name'] = check_and_get_str(request.data, "name")
        check_one_field(request.data, "ingredient")
        check_one_field(request.data, "id")
        try:
            raw_data["ingredient"] = json.loads(request.data["ingredient"])
            dish_data = get_dish_data(raw_data)
            dish_obj = DishSerializer(Dish.objects.get(
                id=request.data["id"]), data=dish_data)
            if dish_obj.is_valid(raise_exception=True):
                dish_obj.save()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))


class DeleteDish(APIviewPlus):
    '''删除菜品'''

    def get_plus(self, request):
        dish_id = check_and_get_str(request.query_params, "id")
        try:
            obj = Dish.objects.get(id=dish_id)
            obj.delete()
            return self.success()
        except Exception as e:
            return self.error(err=str(e))
