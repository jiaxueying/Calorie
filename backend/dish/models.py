from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Dish(models.Model):
    '''菜品'''

    picture = models.ImageField(_("dish picture"), upload_to=None, max_length=100)
    name = models.CharField(_("dish name"), max_length=50)
    calorie = models.IntegerField(_("dish calorie"))
    like = models.IntegerField(_("dish like amount"))
    dislike = models.IntegerField(_("dish dislike amount"))
    tag = models.ManyToManyField("Tag", verbose_name=_("tag"))
    energy = models.DecimalField(_("energy"), max_digits=8, decimal_places=2)
    protein = models.DecimalField(_("protein"), max_digits=8, decimal_places=2)
    fat = models.DecimalField(_("fat"), max_digits=8, decimal_places=2)
    water = models.DecimalField(_("water"), max_digits=8, decimal_places=2)
    carbohydrate = models.DecimalField(_("carbohydrate"), max_digits=8, decimal_places=2)
    sodium = models.DecimalField(_("sodium"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("Dish")
        verbose_name_plural = _("Dishes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Dish_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    '''菜品标签'''

    name = models.CharField(_("tag"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
