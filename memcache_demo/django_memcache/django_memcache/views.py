from django.http import HttpResponse
from django.core.cache import cache


# 操作
def index(request):
    cache.set("username1", "wmm1", 500)
    username = cache.get("username")
    print(username)
    return HttpResponse("成功")
