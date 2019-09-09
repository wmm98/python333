from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm, RegisterForm
from django.views.decorators.http import require_POST


def index(request):
    return HttpResponse("index")


def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # page = form.cleaned_data.get("page")
        # price = form.cleaned_data.get("price")
        # print("title: %s" % title)
        # print("page: %s" % page)
        # print("price: %s" % price)
        # 直接保存到数据库
        form.save()
        return HttpResponse("成功")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("失败")


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        # 不会真正保存到数据库中
        user = form.save(commit=False)
        user.password = form.cleaned_data.get("pwd1")
        user.save()
        return HttpResponse("成功")
    else:
        return HttpResponse("失败")

