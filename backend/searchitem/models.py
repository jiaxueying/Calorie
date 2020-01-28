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

class HistorySearch(models.Model):
    '''搜索历史记录'''
    
    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    searchitem = models.ForeignKey("searchitem.searchitem", verbose_name=_("searchitem"), on_delete=models.CASCADE)
    datetime = models.DateTimeField(_("datetime"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("HistorySearch")
        verbose_name_plural = _("HistorySearches")

    def __str__(self):
        return f'{self.user} searches {self.searchitem} at {time}'

    def get_absolute_url(self):
        return reverse("HistorySearch_detail", kwargs={"pk": self.pk})
