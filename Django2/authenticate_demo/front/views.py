from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Person
from .models import User
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    # 三个参数是必传的
    # user = User.objects.create_user(username="wmm", email="123456@qq.com", password="123456")
    # user = User.objects.create_superuser(username='abc', email='abc@qq.com', password="123456")

    # 修改密码
    # 由于密码是经过加密再存进去的，所以不同于orm语句修改
    # user = User.objects.get(pk=3)
    # print(user.password)
    # user.set_password('111111')
    # user.save()
    # print(user.password)

    # 登录验证
    """
    Django的验证系统已经帮我们实现了登录验证的功能。通过django.contrib.auth.authenticate即可实现。
    这个方法只能通过username和password来进行验证。示例代码如下：

    """
    # username = "wmm"
    # password = "2222"
    # user = authenticate(request, username=username, password=password)
    # if user:
    #     print("登录成功 ", username)
    # else:
    #     print("登录失败")
    return HttpResponse("success")


"""
扩展用户模型：
Django内置的User模型虽然已经足够强大了。但是有时候还是不能满足我们的需求。比如在验证用户登录的时候，他用的是用户名作为验证，
而我们有时候需要通过手机号码或者邮箱来进行验证。还有比如我们想要增加一些新的字段。那么这时候我们就需要扩展用户模型了。
扩展用户模型有多种方式。这里我们来一一讨论下。
"""


# 获取黑名单
def proxy_view(request):
    # blacklist = Person.get_blacklist()
    # for person in blacklist:
    #     print(person.username)
    return HttpResponse("成功")


# 通过手机号码，密码验证
# def my_authenticate(telephone, password):
#     user = User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password)
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None


def one_view(request):
    # 创建数据
    # user = User.objects.create_user(username="mingming", email="ming@qq.com", password="111111")
    # user = User.objects.create_user(username="ming", email="ming1@qq.com", password="111111")
    # user.extension.telephone = "17765602533"
    # user.save()

    # http://127.0.0.1:8000/one_view/?telephone=17765602533&password=111111
    # telephone = request.GET.get("telephone")
    # password = request.GET.get("password")
    # user = my_authenticate(telephone, password)
    # if user:
    #     print("验证成功：", user.username)
    #     # 验证成功： ming
    # else:
    #     print("验证失败")
    return HttpResponse("一对一扩展User模型")


"""
3.对于authenticate不满意，并且不想要修改原来User对象上的一些字段，但是想要增加一些字段，
那么这时候可以直接继承自django.contrib.auth.models.AbstractUser，其实这个类也是django.contrib.auth.models.User的父类。
比如我们想要在原来User模型的基础之上添加一个telephone和school字段。
"""


def inherit_view(request):
    # telephone = '17765602540'
    # password = '123456'
    # username = "小红"
    # user = User.objects.create_user(telephone=telephone, username=username, password=password)
    # print(user.username)

    # telephone = '17765602541'
    # password = '123458'
    # username = "小明"
    # school = "东软学院"
    # user = User.objects.create_superuser(telephone=telephone, username=username, password=password, school=school)
    # print(user.username)

    # telephone = '17765602541'
    # password = '123458'
    # username = "小明"
    # email = "792545884@qq.com"
    # user = User.objects.create_superuser(telephone=telephone,email=email,  username=username, password=password)
    # print(user.username)

    # 验证手机号码
    user = authenticate(request, username="17765602541", password="123458")
    if user:
        print("验证成功")
        print(user.username)
        # 验证成功
        # 小红
    else:
        print("验证失败")
    return HttpResponse("成功继承AbstractUser模型")


# 登录退出以及登录限制案例
# 切记：这里一定不要定义login视图函数
def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            password = form.cleaned_data.get("password")
            remember = form.cleaned_data.get("remember")
            # 验证
            user = authenticate(request, username=telephone, password=password)
            print(telephone)
            if user and user.is_active:
                print("==========================")
                print(telephone, password)
                # 登录之后保存session_id
                login(request, user)
                if remember:
                    # 设置为None则表示使用全局的过期时间
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                # 判断是否会有下页面跳转
                next_url = request.GET.get("next")
                if next_url:
                    # 注意这里没有用到reverse
                    return redirect(next_url)
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse("手机号码或者密码错误")
        else:
            print(form.error)
            return redirect(reverse('login'))


# 退出登录
def my_logout(request):
    logout(request)
    return HttpResponse('退出登录')


@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("这是个人中心")
