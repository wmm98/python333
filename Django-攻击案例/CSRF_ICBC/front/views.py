from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm, TransferForm
from .models import User
from django.db.models import F
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from .decorators import login_required


def index(request):
    return render(request, 'index.html')


# 登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.pk
                # 登录成功后重定向到首页页面
                return redirect(reverse('index'))
            else:
                print("用户名或密码错误")
                return redirect(reverse('login'))
        else:
            print(form.error)
            return redirect(reverse('login'))


# 注册
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(email=email, password=password, username=username, balance=1000)
            return redirect(reverse('login'))
        else:
            return redirect(reverse('register'))


# 转账, 要登录才能进行转账
@method_decorator(login_required, name='dispatch')
class TransferView(View):
    def get(self, request):
        return render(request, 'transfer1.html')

    def post(self, request):
        form = TransferForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            money = form.cleaned_data.get("money")
            # user_id = request.session.get('user_id')
            # user = User.objects.get(pk=user_id)
            # 使用中间件，避免重复
            user = request.front_user
            if user.balance >= money:
                User.objects.filter(email=email).update(balance=F('balance') + money)

                user.balance -= money
                user.save()
                return HttpResponse("转账成功")
            else:
                return HttpResponse("余额不足")
        else:
            print(form.errors)
            # return redirect(reverse("transfer"))
            # 用ajax请求
            return redirect(reverse("transfer"))


# 退出登录
def logout(request):
    # 清除所有的seeion
    request.session.flush()
    return redirect(reverse('index'))
