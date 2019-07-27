from django.urls import path
from . import views

# 当前后台的登陆url都叫login的时候，就会出现错乱，需要用到应用命名空间
# 应用命名空间
# 应用命名空间的变量叫做app_name

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    # 反转url，无论登陆url命名什么都直接跳到login页面
    path('sigin/', views.login, name='login')
]
