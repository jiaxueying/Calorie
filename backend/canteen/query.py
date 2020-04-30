from rest_framework.authtoken.models import Token as authToken
from canteen.models import dish, dish_meta, menu, meta, auth, history, history_meta


def getnames(dish_id):
    lists = dish_meta.objects.filter(dish_id=dish_id)
    names = []
    for x in lists:
        names.append(x.name)
    return names


def getuserid(request):
    token = request.META.get("HTTP_AUTHORIZATION")[6:]
    user_id = authToken.objects.get(key=token).user_id
    return user_id


def gethistory(request):
    user_id = getuserid(request)
    h = []
    lists = history.objects.filter(user_id=user_id)
    for x in lists:
        h.append({
            "id": x.id,
            "time": x.time.strftime("%Y-%m-%d %H:%M:%S"),
            "dishes": []
        })
    for x in h:
        dishes = history_meta.objects.filter(history_id=x["id"])
        for y in dishes:
            z = dish.objects.get(id=y.dish_id)
            x["dishes"].append({
                "img": z.picture.url,
                "dish": z.name,
                "names": getnames(z.id)
            })
    return h


def getdishes(menu_id):
    lists = meta.objects.filter(menu_id=menu_id)
    dishes = []
    for x in lists:
        y = dish.objects.get(id=x.dish_id)
        dishes.append({
            "dish": y.name,
            "dish_id": y.id,
            "img": y.picture.url,
            "num": x.num
        })
    return dishes
