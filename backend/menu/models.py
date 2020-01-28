from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Menu(models.Model):
    '''一餐的菜单'''

    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    date = models.DateField(_("order date"), auto_now=True, auto_now_add=False)
    if_show = models.BooleanField(_("if_show"))

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")

    def __str__(self):
        return f'{self.user} order at {self.date}'

    def get_absolute_url(self):
        return reverse("Menu_detail", kwargs={"pk": self.pk})


class DishOrder(models.Model):
    '''一餐的菜品'''

    dish = models.ForeignKey("dish.Dish", verbose_name=_("dish"), on_delete=models.CASCADE)
    menu = models.ForeignKey("menu.Menu", verbose_name=_("menu"), on_delete=models.CASCADE)
    mass = models.IntegerField(_("amount"))

    class Meta:
        verbose_name = _("DishOrder")
        verbose_name_plural = _("DishOrders")

    def __str__(self):
        return f'{self.menu} has {self.dish} {self.amount}'

    def get_absolute_url(self):
        return reverse("DishOrder_detail", kwargs={"pk": self.pk})
