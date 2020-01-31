from rest_framework import serializers

from dish.models import Dish, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_field = ("id", )


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

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'picture': str(obj.picture),
            'calorie': obj.calorie,
            'carbohydrate': obj.carbohydrate,
            'energy': obj.energy,
            'fat': obj.fat,
            'protein': obj.protein,
            'sodium': obj.sodium,
            'water': obj.water,
            'like': obj.like,
            'dislike': obj.dislike,
            'tag': TagSerializer(obj.tag, many=True).data
        }
