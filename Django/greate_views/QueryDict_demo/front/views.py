from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import QueryDict
from django.views.decorators.http import require_http_methods


def index(request):
    print(type(request.GET))
    print(type(request.POST))
    # <class 'django.http.request.QueryDict'>
    # <class 'django.http.request.QueryDict'>

    # 默认访问第一页,如果不传递任何参数
    username = request.GET.get('p', default=1)
    print(username)
    # 1

    # /?p=2
    # 传递参数的情况下
    # 2
    return HttpResponse("index")


@require_http_methods(['GET', 'POST'])
def add_article(request):
    # get方法：用来获取指定的key值，如果没有这个key,那么就会返回none
    # getlist方法，如果浏览器上传来的key对应的值有多个，那么久需要通过这个方法来获取

    if request.method == 'GET':
        return render(request, "add_article.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        # 获取多个值
        tags = request.POST.getlist("tags")
        print("title:", title)
        print("content:", content)
        print("tags:", tags)
        # title:  ffff
        # content: eeee
        # tags: ['python', 'django']
        return HttpResponse("success")

