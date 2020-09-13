"""
administrate.serializers
"""

from rest_framework import serializers
from administrate.models import Nutrition


class IngredientSerializer(serializers.ModelSerializer):
    '''IngredientSerializer'''

    class Meta:
        model = Nutrition
        fields = "__all__"
        read_only_fields = ["id"]


class OnlyNameIngredientSerializer(serializers.ModelSerializer):
    '''OnlyNameIngredientSerializer'''

    class Meta:
        model = Nutrition
        fields = ["id", "name"]
        read_only_fields = ["id", "name"]
