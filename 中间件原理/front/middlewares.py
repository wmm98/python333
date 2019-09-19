from .models import User


def front_user_middleware(get_response):
    # 执行一些初始化的代码
    print("中间件初始化的一些代码")

    def middleware(request):
        print("request到达view之前执行的一些代码")
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                # 没有登录的情况
                request.front_user = None
        # 没有登录的情况
        else:
            request.front_user = None

        # 在这个代码执行之前的代码，是request到达view之前的代码
        response = get_response(request)
        print("这是response到达浏览器之前执行的代码")
        return response

    return middleware


# 类的形式
class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # 这个中间件初始化的代码

    def __call__(self, request):
        print("request到达view之前执行的一些代码")
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                # 没有登录的情况
                request.front_user = None
        # 没有登录的情况
        else:
            request.front_user = None

        # 在这个代码执行之前的代码，是request到达view之前的代码
        response = self.get_response(request)
        print("这是response到达浏览器之前执行的代码")
        return response
