from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignupForm, SigninForm
from .models import User
# 导入内置处理器
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'sigin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
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
                return redirect(reverse('sigin'))
        else:

            # print(form.errors.get_json_data())
            # 添加错误信息到messages,然后返回给前端
            errors = form.get_error()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('sigin'))


class SignupView(View):
    def get(self, request):
        return render(request, 'sigup.html')

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            errors = form.errors.get_json_data()
            print(errors)
            return redirect(reverse('sigup'))


def blog(request):
    return render(request, "blog.html")


def video(request):
    return render(request, 'video.html')
