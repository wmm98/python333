from django.shortcuts import render
from django.http import HttpResponse


# 1>直接进入url查询
def book(request):
    return HttpResponse('图书馆首页')


def book_detail(request, book_id):
    # 可以从数据库中根据book_id提取这个图书的信息
    text = "您获取的图书id是： %s" % book_id
    return HttpResponse(text)


#  直接字符串查,不用传入参数
def author_detail(request):
    author_id = request.GET.get('id')
    text = '作者的id是： %s' % author_id
    return HttpResponse(text)
