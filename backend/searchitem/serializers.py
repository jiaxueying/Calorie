"""
searchitem.serializers
"""
from rest_framework import serializers
from searchitem.models import SearchItem

class SearchItemSerializer(serializers.ModelSerializer):
    """
    serializer for searchitem.searchitem
    """
    class Meta:
        model = SearchItem
        fields = '__all__'
        read_only_field = ("id", )
