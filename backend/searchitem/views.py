from django.shortcuts import render
from django.shortcuts import get_object_or_404

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

from django.db.models.query import QuerySet
from django.db.models import Count

from searchitem.models import HistorySearch, SearchItem
from searchitem.serializers import SearchItemSerializer

from calorie.api import APIView
from calorie.api import get_user_id
from calorie.api import FieldException, NotImplementedException, NoAttributeInDatabaseException
# Create your views here.


class GetSearchHistoryAPI(APIView):
    def get(self, request):
        user_id = get_user_id(request)
        popular_items = self.get_popular_item()
        history_items = self.get_history_item(user_id)
        return self.success(data={'history_items': history_items, 'popular_items': popular_items})

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
