"""
user.models
数据库设计
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    '''用户'''
    weight = models.IntegerField("user weight", default=60)
    target_weight = models.IntegerField("user target weight", default=60)
    plan = models.BooleanField("if diet", default=False)
    min_calorie = models.DecimalField(
        "user min_calorie", max_digits=8, decimal_places=2, default=100)
    max_calorie = models.DecimalField(
        "user max_calorie", max_digits=8, decimal_places=2, default=2000)
    rate = models.DecimalField(
        "weight change rate", max_digits=8, decimal_places=2, default=0)
    like_dish = models.ManyToManyField(
        "dish.Dish", verbose_name="like_dish", through='LikeDish', through_fields=('user', 'dish'))
    gender = models.CharField(max_length=6, default="male")
    age = models.IntegerField(default=20)
    height = models.IntegerField(default=170)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class LikeDish(models.Model):
    '''用户餐品点赞关联表'''

    user = models.ForeignKey(
        "user.User", verbose_name="user", on_delete=models.CASCADE)
    dish = models.ForeignKey(
        "dish.Dish", verbose_name="dish", on_delete=models.CASCADE)
    like = models.BooleanField("like", null=True)

    class Meta:
        verbose_name = "LikeDish"
        verbose_name_plural = "LikeDishs"

    def __str__(self):
        like_dict = {
            True: 'like',
            False: 'dislike',
            None: 'not comment'
        }
        like = like_dict[self.like]
        return f"{self.user} {like} {self.dish}"
