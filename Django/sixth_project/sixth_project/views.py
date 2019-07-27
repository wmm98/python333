from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def login(request):
    next = request.GET.get('next')
    text = '登陆页面，登陆完成后要跳转的url是： %s' % next
    return HttpResponse(text)


def book(request):
    return HttpResponse('读书页面')


def book_detail(request, book_id, categeory):
    text = '你的图书id是： %s,种类是 %s' % (book_id, categeory)
    return HttpResponse(text)


def movie(request):
    return HttpResponse('电影页面')


def city(request):
    return HttpResponse('同城页面')
