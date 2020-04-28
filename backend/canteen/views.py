"""
canteen.views
"""

import json

from django.db import transaction
from calorie.api import APIView
from calorie.api import check_and_get_str, check_and_get_int, check_one_field, FieldException
from dish.models import Dish
from dish.serializers import DishSerializer
from dish.serializers import DishWithLikeSerializer
from dish.query import DishQueryFunctionSet
from user.models import LikeDish
from django.http import HttpResponse

# Create your views here.


def test(request):
    return HttpResponse("hello")