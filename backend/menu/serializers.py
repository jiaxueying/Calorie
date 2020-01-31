from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'user_id', 'date')
        read_only_field = ("id", )

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'user_id': obj.user_id,
            'date': obj.date,
            # 'picture': obj.dishorder_set.first().dish.picture,
        }
