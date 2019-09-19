# 上下文处理器，登录之后就可以显示用户信息

from .models import User


def front_user(request):
    user_id = request.session.get("user_id")
    print(user_id, '=================')
    context = {}
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            context['front_user'] = user
        except:
            pass
    return context
