from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Person
from .models import User, Article
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, ContentType,Group


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


# 不设置的话会跳转到系统默认的登录url,会报错
@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("这是个人中心")


"""
通过代码添加权限：
权限都是django.contrib.auth.Permission的实例。这个模型包含三个字段，name、codename以及content_type，
其中的content_type表示这个permission是属于哪个app下的哪个models。用Permission模型创建权限的代码如下：
"""


# 通过代码添加权限：
def add_permission(request):
    content_type = ContentType.objects.get_for_model(Article)
    permission = Permission.objects.create(codename='black_article', name='拉黑文章', content_type=content_type)
    return HttpResponse("权限创建成功！")


"""
用户与权限管理：
权限本身只是一个数据，必须和用户进行绑定，才能起到作用。User模型和权限之间的管理，可以通过以下几种方式来管理：

myuser.user_permissions.set(permission_list)：直接给定一个权限的列表。
myuser.user_permissions.add(permission,permission,...)：一个个添加权限。
myuser.user_permissions.remove(permission,permission,...)：一个个删除权限。
myuser.user_permissions.clear()：清除权限。
myuser.has_perm('<app_name>.<codename>')：判断是否拥有某个权限。权限参数是一个字符串，格式是app_name.codename。
myuser.get_all_permissons()：获取所有的权限。
"""


# 操作权限的视图
def operate_permission(request):
    user = User.objects.first()
    # 获取所有跟文章相关的权限
    content_type = ContentType.objects.get_for_model(Article)
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        print(permission)
        # front | article | Can add article
        # front | article | 拉黑文章
        # front | article | Can change article
        # front | article | Can delete article
        # front | article | 看文章的权限

    # myuser.user_permissions.set(permission_list)：直接用户给定一个权限的列表。
    # user.user_permissions.set(permissions)
    # user.save()
    # 清除所有的权限
    # user.user_permissions.clear()

    # myuser.user_permissions.add(permission,permission,...)：一个个添加权限。
    # 添加两个权限
    # user.user_permissions.add(permissions[0], permissions[1])

    # 添加所有权限的另一种表达方式
    # user.user_permissions.add(*permissions)

    # 移除权限，用法跟add一样
    # myuser.user_permissions.remove(permission,permission,...)：一个个删除权限。
    # user.user_permissions.remove(*permissions)

    # 判断是否拥有某个权限。权限参数是一个字符串，格式是app_name.codename。
    # myuser.has_perm('<app_name>.<codename>')：
    # if user.has_perm('front.views_article'):
    #     print("这个用户拥有此权限")
    # else:
    #     print("这个用户没有这个权限")

    # myuser.get_all_permissons()：获取所有的权限。
    print("=======================")
    print(len(user.get_all_permissions()))
    print(user.get_all_permissions())
    # 5
    # {'front.add_article', 'front.change_article', 'front.delete_article', 'front.view_article', 'front.black_article'}

    return HttpResponse("操作权限视图成功")


# 权限管理
# 使用django.contrib.auth.decorators.permission_required可以非常方便的检查用户是否拥有这个权限，如果拥有，
# 那么就可以进入到指定的视图函数中，如果不拥有，那么就会报一个400错误。示例代码如下：
@permission_required('front.add_article', login_url='/login', raise_exception=True)
def add_article(request):
    return HttpResponse("这是添加文章页面")
# 没有权限就无法访问


# 添加分组和赋予权限
def operate_group(request):
    # 1.添加分组
    # group = Group.objects.create(name="运营")
    # content_type = ContentType.objects.get_for_model(Article)
    # permissions = Permission.objects.filter(content_type=content_type)
    # group.permissions.set(permissions)
    # group.save()

    # 2.组内添加员工
    # group = Group.objects.filter(name="运营").first()
    # user = User.objects.first()
    # user.groups.add(group)
    # user.save()

    # 3.获取用户所有的权限
    user = User.objects.first()
    permissions = user.get_group_permissions()
    print(permissions)
    # {'front.change_article', 'front.delete_article', 'front.view_article', 'front.add_article', 'front.black_article'}

    # 4.判断
    # user.has_perm:
    # 1.首先判断user.permissions下有这个权限，如果有就True,
    # 2.如果user.permission下没有这个权限，那么就会判断它所属的分组下有没有这个权限
    # 其作用和 @permission_required('front.add_article)一样

    if user.has_perm('front.add_article'):
        print("有这个添加文章的权限")
    else:
        print("没有添加文章的权限")
    # 有这个添加文章的权限
    return HttpResponse("操作分组")

"""
分组操作：
Group.object.create(group_name)：创建分组。
group.permissions：某个分组上的权限。多对多的关系。

group.permissions.add：添加权限。
group.permissions.remove：移除权限。
group.permissions.clear：清除所有权限。
user.get_group_permissions()：获取用户所属组的权限。
user.groups：某个用户上的所有分组。多对多的关系。
"""


# 在模板中添加权限
def perssions_templates(request):
    return render(request, 'index.html')