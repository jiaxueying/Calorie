from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException, ParseError
from django.db.models.query import QuerySet

from searchitem.models import HistorySearch
from searchitem.models import SearchItem
from django.db.models import Count

from searchitem.serializers import SearchItemSerializer

# Create your views here.

class NotImplementedExecption(APIException):
    status = status.HTTP_501_NOT_IMPLEMENTED
    defualt_detail = '尚未实现该接口'

class FieldException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '该请求需要字段'

class NoAttributeInDatabase(APIException):
    status_code = status.HTTP_501_NOT_IMPLEMENTED
    default_detail = 'This attribute is not in database.'

def get_int(input_data, field_name):
    try:
        return int(input_data)
    except Exception as e:
        raise FieldException(f'{field_name} should be an integer')

def check_one_field(request_data, field_name):
    if field_name not in request_data:
        print(f'{field_name} is required')
        raise FieldException(
            {'msg': f'{field_name} is required'}
        )

def check_and_get_int(request_data, field_name):
    check_one_field(request_data, field_name)
    temp_data = request_data[field_name]
    if isinstance(temp_data, list):
        temp_data = temp_data[0]
    return get_int(temp_data, field_name)
    


class GetSearchHistoryAPI(APIView):
    def get(self, request):
        user_id = self.get_user_id(request)
        popular_items = self.get_popular_item()
        history_items = self.get_history_item(user_id)
        return Response(data={'history_items': history_items, 'popular_items': popular_items}, status=status.HTTP_200_OK)
    
    def get_user_id(self, request):
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

    def get_popular_item(self):
        """
        获取当前热门搜索
        """
        """
        或者直接使用search_time?
        """
        history_searches = HistorySearch.objects.values('searchitem').\
        annotate(count=Count('searchitem')).order_by('-count').\
        values_list('searchitem', flat=True)
        if not history_searches:
            return []
        if len(history_searches) > 10:
            history_searches = history_searches[0:10]    
        serializer = SearchItemSerializer(SearchItem.objects.filter(id__in=history_searches), many=True)
        return serializer.data

    def get_history_item(self, user_id):
        """
        获取用户的历史查询记录
        """
        """
        或者像get_popular_item一样分两个表进行查询
        性能差距? 
        """
        serializer = SearchItemSerializer(SearchItem.objects.filter(historysearch__user__id=user_id), many=True)
        return serializer.data[:10]
