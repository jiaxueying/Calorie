"""
canteen.views
"""

import json as j
from django.db import transaction
from calorie.api import APIView
from django.http import JsonResponse as json, HttpResponse as http, HttpResponseBadRequest as http400, HttpResponseForbidden as http403, HttpResponseNotFound as http404
from rest_framework.authtoken.models import Token as authToken
from canteen.models import dish, dish_meta, menu, meta, auth
from django.core.files.base import ContentFile

# Create your views here.


def permission_veri(request):
    token = request.META.get("HTTP_AUTHORIZATION")[6:]
    user_id = authToken.objects.get(key=token).user_id
    try:
        auth.objects.get(user_id=user_id)
    except:
        return False
    else:
        return True


class test(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            try:
                names = request.POST["names"].split(",")
                return http(names[1])
            except:
                return http("no")


class adddish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            if len(request.FILES) == 1:
                name = request.POST["dish"]
                names = request.POST["names"].split(",")
                img = request.FILES["img"]
                d = dish(
                    name=name,
                    picture=img
                )
                d.save()
                for x in names:
                    dish_meta(dish_id=d.id, name=x).save()
                return http("")


class dishesview(APIView):

    def get(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
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
            return http403("Permission denied")
        else:
            dish_id = request.GET["dish_id"]
            res = {}
            res = {"dish_id": dish_id}
            d = dish.objects.get(id=dish_id)
            res["dish"] = d.name
            res["img"] = d.picture.url
            res["names"] = []
            lists = dish_meta.objects.filter(dish_id=dish_id)
            for x in lists:
                res["names"].append(x.name)
            return json(res)


class deletedish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            dish_id = request.POST["dish_id"]
            d = dish.objects.get(id=dish_id)
            d.delete()
            return http("")


class editdish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            dish_id = request.POST["dish_id"]
            name = request.POST["dish"]
            names = request.POST["names"]
            names = names.split(",")
            try:
                d = dish.objects.get(id=dish_id)
            except:
                return http404("Not found")
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
            return http("")


class menuview(APIView):

    def get(self, request):
        if False:
            return http403("Permission denied")
        else:
            date = request.GET["date"][0:10]
            lists = menu.objects.all()
            for x in lists:
                if x.date.strftime("%Y-%m-%d") == date:
                    if x.period == "bre":
                        mbre = x
                    if x.period == "lun":
                        mlun = x
                    if x.period == "din":
                        mdin = x
            try:
                mbre
            except:
                return http404("Not found")
            bre_ids = meta.objects.filter(menu_id=mbre.id)
            bre = {"menu_id": mbre.id}
            bre["dishes"] = []
            for i in range(len(bre_ids)):
                x = dish.objects.get(id=bre_ids[i].dish_id)
                bre["dishes"].append({})
                bre["dishes"][i] = {}
                bre["dishes"][i]["dish"] = x.name
                bre["dishes"][i]["dish_id"] = x.id
                bre["dishes"][i]["img"] = x.picture.url
                bre["dishes"][i]["num"] = bre_ids[i].num
            lun_ids = meta.objects.filter(menu_id=mlun.id)
            lun = {"menu_id": mlun.id}
            lun["dishes"] = []
            for i in range(len(lun_ids)):
                x = dish.objects.get(id=lun_ids[i].dish_id)
                lun["dishes"].append({})
                lun["dishes"][i] = {}
                lun["dishes"][i]["dish"] = x.name
                lun["dishes"][i]["dish_id"] = x.id
                lun["dishes"][i]["img"] = x.picture.url
                lun["dishes"][i]["num"] = lun_ids[i].num
            din_ids = meta.objects.filter(menu_id=mdin.id)
            din = {"menu_id": mdin.id}
            din["dishes"] = []
            for i in range(len(din_ids)):
                x = dish.objects.get(id=din_ids[i].dish_id)
                din["dishes"].append({})
                din["dishes"][i] = {}
                din["dishes"][i]["dish"] = x.name
                din["dishes"][i]["dish_id"] = x.id
                din["dishes"][i]["img"] = x.picture.url
                din["dishes"][i]["num"] = din_ids[i].num
            menus = {"bre": bre, "lun": lun, "din": din}
            return json(menus)


class addmenu(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            date = request.POST["date"]
            bre = request.POST["bre"].split(",")
            lun = request.POST["lun"].split(",")
            din = request.POST["din"].split(",")
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
            return http("")


class editmenu(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            menu_id = request.POST["menu_id"]
            dish_ids = request.POST["dishes"].split(",")
            lists = meta.objects.filter(menu_id=menu_id)
            for x in lists:
                x.delete()
            for x in dish_ids:
                meta(menu_id=menu_id, dish_id=x).save()
            return http("")


class userdishview(APIView):

    def get(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            menu_id = request.GET["menu_id"]
            dish_id = request.GET["dish_id"]
            if len(meta.objects.filter(menu_id=menu_id, dish_id=dish_id)) == 0:
                return http404("Not found")
            m = menu.objects.get(id=menu_id)
            res = {
                "date": m.date.strftime("%Y-%m-%d"),
                "period": m.period
            }
            d = dish.objects.get(id=dish_id)
            res["dish"] = d.name
            res["img"] = d.picture.url
            lists = dish_meta.objects.filter(dish_id=dish_id)
            names = []
            for x in lists:
                names.append(x.name)
            res["names"] = names
            return json(res)


class orderdish(APIView):

    def post(self, request):
        if not permission_veri(request):
            return http403("Permission denied")
        else:
            orders = request.POST["orders"].split(",")
            for x in orders:
                try:
                    meta.objects.get(
                        menu_id=x["menu_id"], dish_id=x["dish_id"])
                except:
                    return http404("Not found")
            for x in orders:
                d = meta.objects.get(
                    menu_id=x["menu_id"], dish_id=x["dish_id"])
                d.num = d.num+1
                d.save()
            return http("")
