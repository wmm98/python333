from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


# 只能用GET请求来访问这个视图函数
@require_http_methods(['GET'])
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', context={"articles": articles})


@require_http_methods(['GET', 'POST'])
def add_article(request):
    # 如果使用get请求来访问这个视图函数，那么就会返回一个添加文章的HTML页面
    # 如果使用POST请求来访问这个视图函数，那么久获取提交上来的数据，然后保存到数据库中
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        price = request.POST.get("price")
        Article.objects.create(title=title, content=content, price=price)
        return HttpResponse("成功添加数据到数据库")
