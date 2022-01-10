"""
dish.models
数据库设计
"""
from django.db import models

# Create your models here.


class Dish(models.Model):
    '''菜品'''

    picture = models.ImageField("dish picture", max_length=100)
    name = models.CharField("dish name", max_length=50)
    calorie = models.IntegerField("dish calorie")
    weight = models.IntegerField("weight of single product")
    like = models.IntegerField("dish like amount")
    dislike = models.IntegerField("dish dislike amount")
    tag = models.ManyToManyField("Tag", verbose_name="tag")
    energy = models.DecimalField("energy", max_digits=8, decimal_places=2)
    per_calorie = models.DecimalField(
        "calorie per 100g", max_digits=8, decimal_places=2)
    protein = models.DecimalField("protein", max_digits=8, decimal_places=2)
    fat = models.DecimalField("fat", max_digits=8, decimal_places=2)
    carbohydrates = models.DecimalField(
        "carbohydrate", max_digits=8, decimal_places=2)
    sodium = models.DecimalField("sodium", max_digits=8, decimal_places=2)
    dietary_fiber = models.DecimalField(
        "dietary fiber", max_digits=8, decimal_places=2)
    vitaminC = models.DecimalField(
        "Vitamin C", max_digits=8, decimal_places=2)
    calcium = models.DecimalField("calcium", max_digits=8, decimal_places=2)
    views = models.IntegerField("Dish views")
    orders = models.IntegerField("Dish orders")

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''菜品标签'''

    name = models.CharField("tag", max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
