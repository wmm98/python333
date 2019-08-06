from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse


def index(request):
    # 如果没有登陆，那么就重定向到注册页面
    # 如果在url中，传递了username这个参数，那么就认为是登录了，否则就没有登录
    # /username=xxx

    username = request.GET.get("username")
    if username:
        return HttpResponse("首页")
    else:
        return redirect(reverse('singup'))


def singup(request):
    return HttpResponse("注册首页")