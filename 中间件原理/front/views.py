from django.shortcuts import render, reverse, redirect
from .models import User
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse


def index(request):
    print("这是index view中执行的代码")
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse("index")


def my_list(request):
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse("my_list")


class SigninView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # 保存session_id
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            print("用户名或密码错误")
            # messages.add_message(request,messages.INFO, '用户名或密码错误')
            # 等同于
            messages.info(request, '用户名或密码错误')
            return redirect(reverse('login'))
