"""
user.models
数据库设计
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractUser):
    '''用户'''
    weight = models.DecimalField(_("user weight"), max_digits=7, decimal_places=2, default=60)
    target_weight = models.DecimalField(_("user target weight"), max_digits=7, decimal_places=2, default=60)
    plan = models.BooleanField(_("if diet"), default=False)
    min_calorie = models.DecimalField(_("user min_calorie"), max_digits=8, decimal_places=2, default=100)
    max_calorie = models.DecimalField(_("user max_calorie"), max_digits=8, decimal_places=2, default=2000)
    like_dish = models.ManyToManyField("dish.Dish", verbose_name=_("like_dish"), through='LikeDish', through_fields=('user', 'dish'))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username


class LikeDish(models.Model):
    '''用户餐品点赞关联表'''

    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    dish = models.ForeignKey("dish.Dish", verbose_name=_("dish"), on_delete=models.CASCADE)
    like = models.NullBooleanField(_("like"))

    class Meta:
        verbose_name = _("LikeDish")
        verbose_name_plural = _("LikeDishs")

    def __str__(self):
        like_dict = {
            True: 'like',
            False: 'dislike',
            None: 'not comment'
        }
        like = like_dict[self.like]
        return f"{self.user} {like} {self.dish}"
