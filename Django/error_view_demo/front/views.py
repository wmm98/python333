from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse

# 404：服务器没有指定的url。
# 403：没有权限访问相关的数据。
# 405：请求的method错误。
# 400：bad request，请求的参数错误。
# 500：服务器内部错误，一般是代码出bug了。
# 502：一般部署的时候见得比较多，一般是nginx启动了，然后uwsgi有问题。


def index(request):
    # a = 0
    # b = 1
    # c = b / a

    username = request.GET.get('username')
    if not username:
        return redirect(reverse('errors:403'))
    return HttpResponse("首页")


# 错误处理的解决方案：
# 对于404和500这种自动抛出的错误。我们可以直接在templates文件夹下新建相应错误代码的模板文件。
# 而对于其他的错误，我们可以专门定义一个app，用来处理这些错误。




