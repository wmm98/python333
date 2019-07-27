from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Person, Author
from datetime import datetime
from django.utils.timezone import now, localtime


# datatime里的now是个幼稚的时间
# django.utils.timezone import nows不是幼稚的时间
# 默认时间的时候最好不要用default = mow(),这是个固定的时间，一般用default=now

def index(request):
    # article = Article(removed=False, title='很好很好')
    # article.save()

    # article = Article()
    # article.save()

    # article = Article(title='abc', create_time=now())  # 默认当前时间
    # article.save()

    article = Article(title='cdfss')  # 默认当前时间
    article.save()

    # 在settings中设置TIME_ZONE = 'Asia/Shanghai'
    # article = Article.objects.get(pk=5)
    # create_time = article.create_time
    # print('='*30)
    # print(create_time)
    # print(localtime(create_time))
    # print('=' * 30)
    # 2019-07-24 02:26:33.856713+00:00
    # 2019-07-24 10:26:33.856713+08:00

    # article = Article.objects.get(pk=3)
    # print(article)
    # <Article:(3, None, 大数据处理数据,2019-07-12,2019-07-12 11:36:55.734976+00:00,11:36:55.735976)>

    return HttpResponse("success")
    # return render(request, 'index.html', context={'create_time': create_time})


def email(request):
    # p = Person(email='792545884@qq.com')
    # p.save()

    p = Person(email='aaaaaaa')
    p.save()
    return HttpResponse("success")


def unique_view(request):
    author = Author(username='bbbb', telephone='551')
    author.save()
    return HttpResponse("success")