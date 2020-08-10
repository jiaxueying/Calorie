"""
dish.serializers
"""

from rest_framework import serializers

from dish.models import Dish, Tag


class TagSerializer(serializers.ModelSerializer):
    """
    serializer for dish.tag
    """
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_field = ("id", )


class DishMenuSerializer(serializers.ModelSerializer):
    """
    serializer for dish.dish
    """
    class Meta:
        model = Dish
        fields = ('id', 'picture', 'name', 'calorie')
        read_only_field = ("id", )

    # def to_representation(self, instance):
    #     return {
    #         'id': instance.id,
    #         'name': instance.name,
    #         'picture': str(instance.picture),
    #         'calorie': instance.calorie
    #     }


class DishSerializer(serializers.ModelSerializer):
    """
    serializer for dish.dish
    """
    tag = TagSerializer(many=True, read_only=True)
    picture = serializers.ImageField(required=False)

    class Meta:
        model = Dish
        fields = '__all__'
        read_only_field = ("id", )

    # def to_representation(self, instance):
    #     return_data = super().to_representation(instance)
    #     return return_data


class DishWithLikeSerializer(DishSerializer):
    user_like = serializers.BooleanField(
        default=False, initial=False, allow_null=False)
    user_dislike = serializers.BooleanField(
        default=False, initial=False, allow_null=False)

    class Meta:
        model = Dish
        fields = ["id", "picture", "name", "calorie", "like", "dislike", "tag", "energy",
                  "protein", "fat", "carbohydrates", "sodium", "user_like", "user_dislike"]
        read_only_field = ("id", )
