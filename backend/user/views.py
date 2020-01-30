from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView as RestfulAPIView
from calorie.api import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ParseError

from django.http.request import QueryDict

from calorie.api import FieldException
from calorie.api import NotImplementedExecption
from calorie.api import NoAttributeInDatabaseException

from calorie.api import get_int
from calorie.api import check_one_field
from calorie.api import check_and_get_int

from calorie.settings import DEBUG

def get_user_id(request):
    request_data = request.query_params
    """
    如果使用原生的django用户, 可以通过request.user拿到用户对象
    尝试该项目是否可以使用此法
    """
    user_id = None
    try:
        user_id = request.user.id
        assert (user_id is not None)
    except Exception as e:
        print("无法获取request.user.id")
        user_id = check_and_get_int(request_data, 'user_id')
    return user_id

from rest_framework.authtoken import views as rest_auth
from copy import copy
from copy import deepcopy

class UserLoginAPI(rest_auth.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
        Login API
        """
        # Add something for miniapp
        # Django just need two key-value -- username and password -- in request.data
        login_data = copy(request.data)
        try:
            assert(login_data['code'] is not None)
        except Exception as e:
            print('没有code')
            if DEBUG:
                return super().post(request, args, kwargs)
            else:
                return Response(data={'msg': '登录失败'}, status=status.HTTP_401_UNAUTHORIZED) # 401.1?
        else:
            print('有code')
            login_data['username'] = self.get_openid(login_data['code'])
            login_data['password'] = self.get_password(login_data['username'])
            serializer = self.serializer_class(data=login_data,context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

    def get_openid(self, code):
        """
        向微信接口请求openid
        """
        # 注意可能超时和其他的异常
        return code

    def get_password(self, username):
        """
        得到登录密码
        """
        return username



# Create your views here.
