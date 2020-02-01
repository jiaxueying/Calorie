"""
user.serializers
"""
from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user.user
    """
    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ("id", )
