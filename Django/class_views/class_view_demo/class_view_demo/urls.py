"""class_view_demo URL Configuration

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

from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('BookListView/', views.BookListView.as_view(), name='BookListView'),
    path("AddBookView/", views.AddBookView.as_view(), name='AddBookView'),
    path('BookDetail/<book_id>/', views.BookDetail.as_view(), name='BookDetail'),
    # 以后如果渲染的这个模板不需要传递任何的参数，那么建议在urls中使用TempaltesView
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    # 如果非要传递参数
    path('AboutView/', views.AboutView.as_view(), name='AboutView'),
    path('article/', include('front.urls'))
]
