"""
canteen.models
数据库设计
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class dish(models.Model):
    '''套餐'''

    picture = models.ImageField(
        _("dish picture"), upload_to="canteen", max_length=100)
    name = models.CharField(_("dish name"), max_length=50)
    calorie = models.IntegerField(_("dish calorie"), default=0)

    class Meta:
        verbose_name = _("dish")
        verbose_name_plural = _("dishes")

    def __str__(self):
        return self.name


class dish_meta(models.Model):
    '''套餐详情'''

    dish = models.ForeignKey(dish, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("dish_meta")
        verbose_name_plural = _("dish_metas")

    def __str__(self):
        return self.name


class menu(models.Model):
    '''菜单'''

    date = models.DateTimeField()
    period = models.CharField(max_length=3)

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def __str__(self):
        return self.name


class meta(models.Model):
    '''菜单详情'''

    menu = models.ForeignKey(menu, on_delete=models.CASCADE)
    dish = models.ForeignKey(dish, on_delete=models.CASCADE)
    num = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("meta")
        verbose_name_plural = _("metas")

    def __str__(self):
        return self.name


class auth(models.Model):
    '''授权用户'''

    user_id = models.IntegerField()

    def __str__(self):
        return self.name


class history(models.Model):
    '''历史菜单'''

    user_id = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name


class history_meta(models.Model):
    '''历史菜单详情'''

    history = models.ForeignKey(history, on_delete=models.CASCADE)
    dish = models.ForeignKey(dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
