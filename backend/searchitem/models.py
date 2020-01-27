from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SearchItem(models.Model):
    '''搜索条目'''

    name = models.CharField(_("search item"), max_length=50)
    search_time = models.IntegerField(_("search_time"))

    class Meta:
        verbose_name = _("SearchItem")
        verbose_name_plural = _("SearchItems")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SearchItem_detail", kwargs={"pk": self.pk})
