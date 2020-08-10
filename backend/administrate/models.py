'''
administrate.models
'''

from django.db import models


class Nutrition(models.Model):
    '''营养成分表'''

    name = models.CharField(max_length=50)
    calorie = models.IntegerField()
    energy = models.IntegerField()
    protein = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fat = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    carbohydrates = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    dietary_fiber = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    vitaminC = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    calcium = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sodium = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class Auth(models.Model):
    '''已授权用户'''

    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Token(models.Model):
    '''身份令牌'''

    auth_id = models.IntegerField()
    expiration = models.DateTimeField()
    token = models.CharField(max_length=32)
