from rest_framework import serializers

from dish.models import Dish


class DishMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'picture', 'name', 'calorie')
        read_only_field = ("id", )

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'picture': str(obj.picture),
            'calorie': obj.calorie
        }


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        read_only_field = ("id", )