from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def index(request):
    # 如果没有登陆就跳转到登陆页面
    #  ?username=xxx
    userName = request.GET.get('userName')
    if userName:
        return HttpResponse('前台首页')
    else:
        # return redirect('/login/')

        # 可以任意改url,都会跳转到login页面
        # login_url = reverse('login')

        # 应用命名空间指定
        login_url = reverse('front:login')
        return redirect(login_url)


def login(request):
    return HttpResponse('前台登陆页面')
