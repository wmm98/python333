from django.urls import re_path
from . import views

urlpatterns = [
    # r"" 代表使原生字符串(raw)
    re_path(r'^$', views.article),  # "^$"=""代表空的意思
    # article/list/<year>/
    re_path(r'^list/(?P<year>\d{4})/$', views.article_list)
]

# ^list表示以list开头，?P表示捕获一个变量，<year>传入的参数，\d表示为0到9的整数，{4}表示取4位，/$表示以/结束
