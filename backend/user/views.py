"""
详细文档在后期完善
user.view 描述和用户相关的API
"""
import json
from copy import copy
import requests
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views as rest_auth
from rest_framework.permissions import AllowAny

from calorie.api import APIView
from calorie.api import FieldException, NetworkConnectionException
from calorie.settings import DEBUG

from user.serializers import UserSerializer
from user.models import User

APPSECRET = "987fa4e0b2d2198e83a760a42b42148c"
APPID = "wx6310320ccdaaf1c5"
GRANT_TYPE = "authorization_code"

class UserLoginAPI(rest_auth.ObtainAuthToken):
    """
    该API用于用户登录，继承自rfw的rest_auth.ObtainAuthToken，将用于认证身份的token发给前端
    """
    def post(self, request, *args, **kwargs):
        """
        Login API
        request - 前端发来的请求
        """
        login_data = copy(request.data)
        try:
            assert login_data['code'] is not None
        except MultiValueDictKeyError as _:
            # 没有code
            if DEBUG:
                return super().post(request, *args, **kwargs)
            return Response(data={'msg': '登录失败'}, status=status.HTTP_401_UNAUTHORIZED) # 401.1?
        else:
            # 有code
            login_data['username'] = self.get_openid(login_data['code'])
            login_data['password'] = self.get_password(login_data['username'])
            if not User.objects.filter(username=login_data['username']):
                User.objects.create_user(username=login_data['username'], password=login_data['password'], name=login_data['name'])
            return self.get_or_create_token(login_data, request)

    @staticmethod
    def get_openid(code):
        """
        向微信接口请求openid
        code - 前端通过wx.login得到的code
        """
        # 注意可能超时和其他的异常
        url = f"https://api.weixin.qq.com/sns/jscode2session?APPID={APPID}&secret={APPSECRET}&js_code={code}&GRANT_TYPE={GRANT_TYPE}"
        response = requests.get(url=url)
        if response.status_code == 200:
            content = json.loads(response.content)
            try:
                return content['openid']
            except Exception as _:
                print("content没有openid")
                raise FieldException("content没有openid")
        raise NetworkConnectionException()

    @staticmethod
    def get_password(username):
        """
        得到登录密码
        """
        return username

    def get_or_create_token(self, login_data, request):
        """
        返回认证用token
        """
        serializer = self.serializer_class(data=login_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class UserProfileAPI(APIView):
    """
    该API用于获取或者修改用户信息
    """
    def post(self, request):
        """
        修改用户信息
        """
        required_fields = ('weight', )
        for required_field in required_fields:
            if required_field not in request.data:
                raise FieldException("没有字段%s"%required_field)
        user_obj = request.user
        user_obj.weight = request.data['weight']
        user_obj.save()
        return self.success()

    def get(self, request):
        """
        获取用户信息
        """
        user_obj = request.user
        serializer = UserSerializer(user_obj)
        try:
            return self.success(data=serializer.data)
        except Exception as _:
            return self.error(err=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
