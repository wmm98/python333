from django.http import HttpResponse
from django.shortcuts import reverse, redirect


def index(request):
    # http://127.0.0.1:8000/?username=mmmm 查询字符串模式
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        # login_url = reverse('login')
        # return redirect(login_url)

        # 跳转到文章详情页面
        # detail_url = reverse('detail', kwargs={'article_id': 1})
        # return redirect(detail_url)

        # 跳转到带有查询字符串的页面
        login_url = reverse('login') + "?next=/"
        return redirect(login_url)


def login(request):
    return HttpResponse("登陆首页")


def article_detail(request, article_id):
    text = "您的文章id是： %s" % article_id
    return HttpResponse(text)

