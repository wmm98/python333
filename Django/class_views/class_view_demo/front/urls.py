from django.urls import path, include
from . import views

app_name = 'front'
urlpatterns = [
    path("add_article/", views.add_article, name='add_article'),
    path('article_list/', views.article_list.as_view(), name='article_list'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.login, name='login')
]
