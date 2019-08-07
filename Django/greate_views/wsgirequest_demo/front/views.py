from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIHandler


def index(request):
    print(type(request))
    # <class 'django.core.handlers.wsgi.WSGIRequest'>
    return HttpResponse("index")


def login(request):
    # 获取路径
    # print(request.path)
    # print(request.get_full_path())
    # /login/
    # /login/
    # print(request.get_raw_uri())
    # http://127.0.0.1:8000/login/
    print("******************************************")
    # get_host()
    # 返回服务器域名，如果在访问的的时候还有端口号，那么会加上端口号
    # print(request.get_host())
    # 127.0.0.1:8000

    # 是否为http协议s
    # print(request.is_secure())
    # False

    # is_ajax():是否采用ajax发送的请求，原理就是判断请求中是否存在 X-Requested-With:XMLHttpRequest
    print(request.is_ajax())
    # True
    print(  "*******************************************")
    # 获取头部信息
    # for key, value in request.META.items():
    #     print(key, " ", value)
    # return HttpResponse("login")
