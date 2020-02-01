"""
menu.serializers
"""
from rest_framework import serializers
from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    serializer for menu.menu
    """
    class Meta:
        model = Menu
        fields = ('id', 'user_id', 'date')
        read_only_field = ("id", )

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user_id': instance.user_id,
            'date': instance.date,
            'picture': str(instance.dishorder_set.first().dish.picture),
        }
