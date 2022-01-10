'''
dish.api
'''

import random
from user.models import User
from dish.models import Dish
from dish.serializers import DishSerializer


def recommend():
    last = Dish.objects.count()-1
    index1 = random.randint(0, last)
    index2 = random.randint(0, last-1)
    if index1 == index2:
        index1 = last
    dish1 = DishSerializer(Dish.objects.all()[index1]).data
    dish2 = DishSerializer(Dish.objects.all()[index2]).data
    dishes = {"dishes": [dish1, dish2]}
    return dishes
