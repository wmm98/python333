from django.urls import path
from . import views
app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('one_to_many_view/', views.one_to_many_view, name='one_to_many_view'),
    path('delete_view/', views.delete_view, name='delete_view'),
    path('one_to_one_view/', views.one_to_one_view, name='one_to_one_view'),
    path('many_to_many_view/', views.many_to_many_view, name='many_to_many_view')
]
