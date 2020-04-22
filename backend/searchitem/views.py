"""
searchitem.views
"""
from django.db.models import Count

from calorie.api import APIView
from calorie.api import get_user_id
from searchitem.models import HistorySearch, SearchItem
from searchitem.serializers import SearchItemSerializer

# Create your views here.

class GetSearchHistoryAPI(APIView):
    """
    获得当前热门搜索和历史查询记录的api
    """
    def get(self, request):
        """
        获得当前热门搜索和历史查询记录的api
        """
        user_id = get_user_id(request)
        popular_items = self.get_popular_item()
        history_items = self.get_history_item(user_id)
        return self.success(data={'history_items': history_items, 'popular_items': popular_items})

    @staticmethod
    def get_popular_item():
        """
        获取当前热门搜索
        """
        serializer = SearchItemSerializer(
            SearchItem.objects.filter(
                id__in=HistorySearch.objects.values('searchitem').annotate(count=Count('searchitem')).order_by('-count').values_list('searchitem', flat=True)
            ), many=True
        )
        return serializer.data[:10]

    @staticmethod
    def get_history_item(user_id):
        """
        获取用户的历史查询记录
        """
        # 或者像get_popular_item一样分两个表进行查询，有性能差距吗
        history = HistorySearch.objects.filter(user=user_id).order_by('-datetime').values_list('searchitem', flat=True)
        history = list(dict.fromkeys(history, 0))[:10]
        serializer = SearchItemSerializer(
            SearchItem.objects.filter(
                id__in=history
            ), many=True
        )
        return serializer.data
