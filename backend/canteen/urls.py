"""
canteen.urls
"""
# views is used to log in
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test.as_view()),
    path('adddish/', views.adddish.as_view()),
    path('dishesview/', views.dishesview.as_view()),
    path('dishview/', views.dishview.as_view()),
    path('deletedish/', views.deletedish.as_view()),
    path('editdish/', views.editdish.as_view()),
    path('menuview/', views.menuview.as_view()),
    path('addmenu/', views.addmenu.as_view()),
    path('editmenu/', views.editmenu.as_view()),
    path('userdishview/', views.userdishview.as_view()),
    path('orderdish/', views.orderdish.as_view()),
    path('historyview/', views.historyview.as_view()),
    path('deletehistory/', views.deletehistory.as_view()),
]
