"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.http import HttpResponse


# 打开 http://127.0.0.1:8000/的时候就不会出错
def index(request):
    return HttpResponse("首页")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('book/', views.book),
    # 可以手动在地址上写id，然后救会跳转 <book_id>为url中传入的参数
    # 例如： /book/detail/1
    path('book/detail/<book_id>/', views.book_detail),
    # 字符串进行查询 ；例如：/book/author/?id=1
    path('book/author/', views.author_detail)
]
