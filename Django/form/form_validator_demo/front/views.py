from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import MyForm, RegisterForm
from .models import User


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            print(telephone)
            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            # {'email': [{'message': '请输入正确的邮箱', 'code': 'invalid'}]}
            return HttpResponse("fail")


"""
FloatField：
用来接收浮点类型，并且如果验证通过后，会将这个字段的值转换为浮点类型。
参数：

max_value：最大的值。
min_value：最小的值。
错误信息的key：required、invalid、max_value、min_value。

IntegerField：
用来接收整形，并且验证通过后，会将这个字段的值转换为整形。
参数：

max_value：最大的值。
min_value：最小的值。
错误信息的key：required、invalid、max_value、min_value。

URLField：
用来接收url格式的字符串。
错误信息的key：required、invalid。
"""


# 自定义验证块
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            User.objects.create(username=username, telephone=telephone)
            return HttpResponse("注册成功")
        else:
            # print(form.errors.get_json_data())
            # {'telephone': [{'message': '请输入正确手机号码', 'code': 'invalid'}], 'pwd1':
            # [{'message': 'Ensure this value has at least 6 characters (it has 5).', 'code': 'min_length'}],
            # '__all__': [{'message': '两次输入密码不一致', 'code': ''}]}
            print(form.get_errors())
            """
            {'telephone': ['请输入正确手机号码'], 
            'pwd1': ['Ensure this value has at least 6 characters (it has 5).'], 
            'pwd2': ['Ensure this value has at least 6 characters (it has 5).']}
            """
            return HttpResponse("注册失败")

