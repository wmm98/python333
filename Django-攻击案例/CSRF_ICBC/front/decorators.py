from .models import User
from django.shortcuts import reverse, redirect


# 装饰器
def login_required(func):
    def wrapper(request, *args, **kwargs):
        # # 获取user_id
        # user_id = request.session.get('user_id')
        # exists = User.objects.filter(pk=user_id).exists()

        # 因为是先执行中间件，所以可以直接使用request.front_user
        if request.front_user:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))
    return wrapper