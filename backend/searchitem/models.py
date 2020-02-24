"""
searchitem.models
数据库设计
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SearchItem(models.Model):
    '''搜索条目'''
    SEARCH_CATEGORYS = [
        ('keyword', 'keyword'),
        ('tag', 'tag'),
    ]
    name = models.CharField(_("search item"), max_length=50)
    count = models.IntegerField(_("search count"), default=0)
    category = models.CharField(_("search category"), choices=SEARCH_CATEGORYS, max_length=10)

    class Meta:
        verbose_name = _("SearchItem")
        verbose_name_plural = _("SearchItems")

    def __str__(self):
        return self.name

class HistorySearch(models.Model):
    '''搜索历史记录'''

    user = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    searchitem = models.ForeignKey("searchitem.searchitem", verbose_name=_("searchitem"), on_delete=models.CASCADE)
    datetime = models.DateTimeField(_("datetime"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("HistorySearch")
        verbose_name_plural = _("HistorySearches")

    def __str__(self):
        return f'{self.user} searches {self.searchitem} at {self.datetime}'
