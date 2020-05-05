"""
canteen.views
"""

import time
import json as j
from django.db import transaction
from calorie.api import APIView
from django.http import JsonResponse as json, HttpResponse as http, HttpResponseBadRequest as http400, HttpResponseForbidden as http403, HttpResponseNotFound as http404, HttpResponseServerError as http500
from rest_framework.authtoken.models import Token as authToken
from canteen.models import dish, dish_meta, menu, meta, auth, history, history_meta
from django.core.files.base import ContentFile
from . import query

# Create your views here.

# 辅助函数


def permission_veri(request):
    user_id = query.getuserid(request)
    try:
        auth.objects.get(user_id=user_id)
    except:
        return False
    else:
        return True


def getdate(obj):
    return obj.date.strftime("%Y-%m-%d")

# APIs


class test(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            names = request.POST.get("names")
            names = j.loads(names)
            return http(names[0])


class adddish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            if len(request.FILES) == 1:
                try:
                    name = request.POST["dish"]
                    names = j.loads(request.POST["names"])
                except:
                    return http400("参数不完整")
                img = request.FILES["img"]
                d = dish(
                    name=name,
                    picture=img
                )
                d.save()
                for x in names:
                    dish_meta(dish_id=d.id, name=x).save()
                return http("添加成功")
            else:
                return http400("未接收到图片")


class dishesview(APIView):

    def get(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            res = {}
            lists = dish.objects.all()
            res["dishes"] = []
            for i in range(len(lists)):
                res["dishes"].append({})
                res["dishes"][i]["dish"] = lists[i].name
                res["dishes"][i]["dish_id"] = lists[i].id
                res["dishes"][i]["img"] = lists[i].picture.url
            return json(res)


class dishview(APIView):

    def get(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            try:
                dish_id = request.GET["dish_id"]
            except:
                return http400("参数不完整")
            res = {}
            res = {"dish_id": dish_id}
            try:
                d = dish.objects.get(id=dish_id)
            except:
                return http404("该套餐不存在")
            res["dish"] = d.name
            res["img"] = d.picture.url
            res["names"] = query.getnames(dish_id)
            return json(res)


class deletedish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            try:
                dish_id = request.POST["dish_id"]
            except:
                return http400("参数不完整")
            try:
                d = dish.objects.get(id=dish_id)
            except:
                return http404("该套餐不存在")
            d.delete()
            return http("删除成功")


class editdish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            try:
                dish_id = request.POST["dish_id"]
                name = request.POST["dish"]
                names = request.POST["names"]
            except:
                return http400("参数不完整")
            names = j.loads(names)
            try:
                d = dish.objects.get(id=dish_id)
            except:
                return http404("该套餐不存在")
            d.name = name
            d.save()
            lists = dish_meta.objects.filter(dish_id=dish_id)
            for x in lists:
                x.delete()
            for x in names:
                y = dish_meta(dish_id=dish_id, name=x)
                y.save()
            if len(request.FILES) == 1:
                img = request.FILES["img"]
                d.picture = img
                d.save()
            return http("修改成功")


def menuview(request):
    if False:
        return http403("没有权限")
    else:
        try:
            date = request.GET["date"][0:10]
        except:
            return http400("参数不完整")
        lists = menu.objects.all()
        for x in lists:
            if getdate(x) == date:
                if x.period == "bre":
                    mbre = x
                if x.period == "lun":
                    mlun = x
                if x.period == "din":
                    mdin = x
        try:
            mbre
        except:
            return http404("当天菜单不存在")
        bre = {"menu_id": mbre.id}
        lun = {"menu_id": mlun.id}
        din = {"menu_id": mdin.id}
        bre["dishes"] = query.getdishes(mbre.id)
        lun["dishes"] = query.getdishes(mlun.id)
        din["dishes"] = query.getdishes(mdin.id)
        menus = {"bre": bre, "lun": lun, "din": din}
        return json(menus)


class addmenu(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            try:
                date = request.POST["date"][0:10]
                bre = j.loads(request.POST["bre"])
                lun = j.loads(request.POST["lun"])
                din = j.loads(request.POST["din"])
            except:
                return http400("参数不完整")
            m = menu.objects.all()
            for x in m:
                if getdate(x) == date:
                    return http500("当天菜单已存在")
            for x in bre:
                try:
                    dish.objects.get(id=x)
                except:
                    return http404("dish_id:"+x+"不存在")
            for x in lun:
                try:
                    dish.objects.get(id=x)
                except:
                    return http404("dish_id:"+x+"不存在")
            for x in din:
                try:
                    dish.objects.get(id=x)
                except:
                    return http404("dish_id:"+x+"不存在")
            mbre = menu(date=date, period="bre")
            mbre.save()
            bre_id = mbre.id
            mlun = menu(date=date, period="lun")
            mlun.save()
            lun_id = mlun.id
            mdin = menu(date=date, period="din")
            mdin.save()
            din_id = mdin.id
            for x in bre:
                meta(dish_id=x, menu_id=bre_id).save()
            for x in lun:
                meta(dish_id=x, menu_id=lun_id).save()
            for x in din:
                meta(dish_id=x, menu_id=din_id).save()
            return http("添加成功")


class editmenu(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("没有权限")
        else:
            try:
                menu_id = request.POST["menu_id"]
                dish_ids = j.loads(request.POST["dishes"])
            except:
                return http400("参数不完整")
            try:
                menu.objects.get(id=menu_id)
            except:
                return http404("菜单不存在")
            for x in dish_ids:
                try:
                    dish.objects.get(id=x)
                except:
                    return http404("dish_id:"+x+"不存在")
            lists = meta.objects.filter(menu_id=menu_id)
            for x in lists:
                x.delete()
            for x in dish_ids:
                meta(menu_id=menu_id, dish_id=x).save()
            return http("修改成功")


def userdishview(request):
    if False:
        return http403("没有权限")
    else:
        try:
            menu_id = request.GET["menu_id"]
            dish_id = request.GET["dish_id"]
        except:
            return http400("参数不完整")
        if len(meta.objects.filter(menu_id=menu_id, dish_id=dish_id)) == 0:
            return http404("当日该套餐不存在")
        m = menu.objects.get(id=menu_id)
        res = {
            "date": getdate(m),
            "period": m.period
        }
        d = dish.objects.get(id=dish_id)
        res["dish"] = d.name
        res["img"] = d.picture.url
        res["names"] = query.getnames(d.id)
        return json(res)


class orderdish(APIView):

    def post(self, request):
        if False:
            return http403("没有权限")
        else:
            try:
                orders = j.loads(request.POST["orders"])
            except:
                return http400("参数不完整")
            for x in orders:
                try:
                    meta.objects.get(
                        menu_id=x["menu_id"], dish_id=x["dish_id"])
                except:
                    return http404("当日该套餐不存在")
            h = history(
                user_id=query.getuserid(request),
                time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            )
            h.save()
            for x in orders:
                d = meta.objects.get(
                    menu_id=x["menu_id"], dish_id=x["dish_id"])
                d.num = d.num+1
                d.save()
                history_meta(history_id=h.id, dish_id=x["dish_id"]).save()
            return http("点餐成功")


class historyview(APIView):

    def get(self, request):
        if False:
            return http403("没有权限")
        else:
            h = query.gethistory(request)
            return json({"history": h})


class deletehistory(APIView):

    def post(self, request):
        if False:
            return http403("没有权限")
        else:
            try:
                history_id = request.POST["history_id"]
            except:
                return http400("参数不完整")
            try:
                history.objects.get(
                    id=history_id, user_id=query.getuserid(request)).delete()
            except:
                return http404("记录不存在")
            else:
                return http("删除成功")
