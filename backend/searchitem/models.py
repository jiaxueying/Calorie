"""
searchitem.models
数据库设计
"""
from django.db import models

# Create your models here.


class SearchItem(models.Model):
    '''搜索条目'''
    SEARCH_CATEGORYS = [
        ('keyword', 'keyword'),
        ('tag', 'tag'),
    ]
    name = models.CharField("search item", max_length=50)
    count = models.IntegerField("search count", default=0)
    category = models.CharField("search category", choices=SEARCH_CATEGORYS, max_length=10)

    class Meta:
        verbose_name = "SearchItem"
        verbose_name_plural = "SearchItems"

    def __str__(self):
        return self.name

class HistorySearch(models.Model):
    '''搜索历史记录'''

    user = models.ForeignKey("user.User", verbose_name="user", on_delete=models.CASCADE)
    searchitem = models.ForeignKey("searchitem.searchitem", verbose_name="searchitem", on_delete=models.CASCADE)
    datetime = models.DateTimeField("datetime", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "HistorySearch"
        verbose_name_plural = "HistorySearches"

    def __str__(self):
        return f'{self.user} searches {self.searchitem} at {self.datetime}'
