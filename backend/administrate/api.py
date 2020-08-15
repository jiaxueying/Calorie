'''
administrate.api
'''

from datetime import datetime, timedelta
from random import shuffle
from dateutil import tz
from calorie.api import APIView
from administrate.models import Token, Nutrition
from administrate.serializers import IngredientSerializer


class APIviewPlus(APIView):
    '''继承APIview，实现后台权限验证'''

    def get_plus(self, request):
        '''新get方法'''
        return self.error(err="请使用post方法")

    def post_plus(self, request):
        '''新post方法'''
        return self.error(err="请使用get方法")

    def get(self, request):
        '''原get方法'''

        token = request.META.get("HTTP_ADMINISTRATOR_TOKEN")
        if token is None:
            return self.error("请提供后台身份验证信息")

        if AuthToken.auth(token):
            return self.get_plus(request)
        else:
            return self.error(err="Auth time out!")

    def post(self, request):
        '''原post方法'''

        token = request.META.get("HTTP_ADMINISTRATOR_TOKEN")
        if token is None:
            return self.error("请提供后台身份验证信息")

        if AuthToken.auth(token):
            return self.post_plus(request)
        else:
            return self.error(err="Auth time out!")


class AuthToken:
    '''token管理工具'''

    @staticmethod
    def __expiration():
        '''获取30分钟后的时间'''

        return datetime.now(tz=tz.gettz("Asia/Shanghai"))+timedelta(minutes=30)

    @staticmethod
    def update_token(auth_id):
        '''更新用户token'''

        string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        str_list = list(string)
        shuffle(str_list)
        string = ''.join(str_list)
        token = string[0:32]
        record = Token.objects.filter(auth_id=auth_id)
        if not record:
            Token.objects.create(
                auth_id=auth_id, expiration=AuthToken.__expiration(), token=token)
        else:
            record[0].token = token
            record[0].expiration = AuthToken.__expiration()
            record[0].save()
        return token

    @staticmethod
    def auth(token):
        '''鉴权并更新token有效期'''

        record = Token.objects.filter(token=token)
        if not record:
            return False
        if datetime.now(tz=tz.gettz("Asia/Shanghai")).__ge__(record[0].expiration):
            return False
        else:
            record[0].expiration = AuthToken.__expiration()
            record[0].save()
            return True


def get_dish_data(raw_data):
    '''把获取的原始数据转换成可被序列化的数据'''

    items = ['calorie', 'energy', 'protein', 'fat', 'carbohydrates',
             'sodium', 'dietary_fiber', 'vitaminC', 'calcium']
    dish_data = {
        'name': raw_data['name'],
        'like': 0,
        'dislike': 0
    }
    try:
        dish_data['picture'] = raw_data['picture']
    except Exception:
        pass

    for i in items:
        dish_data[i] = 0

    weight = 0
    for ingredient in raw_data['ingredient']:
        obj = Nutrition.objects.get(id=ingredient['id'])
        ingredient_data = IngredientSerializer(obj).data
        per = int(ingredient['weight'])/100
        weight += int(ingredient['weight'])
        for i in items:
            dish_data[i] += float(ingredient_data[i])*per

    dish_data['weight'] = weight
    per = 100/weight
    for i in items:
        dish_data[i] *= per

    return dish_data
