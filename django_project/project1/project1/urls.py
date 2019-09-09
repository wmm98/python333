"""project1 URL Configuration

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
from front import views


urlpatterns = [
    path('', views.index),
    # path('save_background_address/', views.save_background_address),
    # path('get_data/', views.get_data),
    # path('deal_data/', views.deal_data),
    # path('models_data/', views.models_data),
    # path('save_img/', views.save_img_address),
    path('get_city/', views.get_city),
    path('test_get_data/', views.test_get_data)

]
