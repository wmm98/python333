"""authenticate_demo URL Configuration

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
from front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blacklist/', views.proxy_view, name='blacklist'),
    path('one_view/', views.one_view, name="one_view"),
    path('inherit_view/', views.inherit_view, name='inherit_view'),
    path("login/", views.my_login, name="login"),
    path("logout/", views.my_logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('permission/', views.add_permission, name='add_permission'),
    path('operate_permission/', views.operate_permission, name='operate_permission'),
    path('add_article/', views.add_article, name='add_article'),
    path('operate_group/', views.operate_group, name="operate_group"),
    path("perssions_templates/", views.perssions_templates, name="perssions_templates")
]
