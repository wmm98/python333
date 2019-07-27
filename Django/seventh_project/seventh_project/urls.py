"""seventh_project URL Configuration

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

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_view, name='add'),
    path('add_list/', views.add_list, name='add_list'),
    path('cut_view/', views.cut_view, name='cut_view'),
    path('date_view/', views.date_view, name='date_view'),
    path('default_view/', views.default_view, name='default_view'),
    path('first_last_view/', views.first_last_view, name='first_last_view'),
    path('floatformat_view/', views.floatformat_view, name='floatformat_view'),
    path('join_view/', views.join_view, name='join_view'),
    path('lower/', views.lower, name='lower'),
    path('random_view/', views.random_view, name='random_view'),
    path('safe_view/', views.safe_view, name='safe_view'),
    path('slice_view/', views.slice_view, name='slice_view'),
    path('striptags_view/', views.striptags_view, name='striptags_view'),
    path('truncatechars_view/', views.truncatechars_view, name='truncatechars_view'),
    path('truncatechars_html_view/', views.truncatechars_html_view, name='truncatechars_html_view')

]
