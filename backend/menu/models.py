from django.db import models

# Create your models here.


class Menu(models.Model):
    '''一餐的菜单'''

    user = models.ForeignKey("user.User", verbose_name="user", on_delete=models.CASCADE)
    date = models.DateTimeField("order date", auto_now=True, auto_now_add=False)
    if_show = models.BooleanField("if_show")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f'{self.user} order at {self.date}'

class DishOrder(models.Model):
    '''一餐的菜品'''

    dish = models.ForeignKey("dish.Dish", verbose_name="dish", on_delete=models.CASCADE)
    menu = models.ForeignKey("menu.Menu", verbose_name="menu", on_delete=models.CASCADE)
    mass = models.IntegerField("amount")

    class Meta:
        verbose_name = "DishOrder"
        verbose_name_plural = "DishOrders"

    def __str__(self):
        return f'{self.menu} has {self.dish} {self.mass}'
