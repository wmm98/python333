from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.article),
    # \w: 0-9, a-z, A-Z  \+代表单纯的加号
    # 例如
    # list/python
    # list/python+django/
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/', views.article_list),

    path("list/<cate:categories>/", views.article_list, name='list'),
    path('detail/<int:article_id>/', views.article_detail, name='detail')
]
