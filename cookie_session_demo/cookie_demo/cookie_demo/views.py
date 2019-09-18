from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

"""
设置cookie：
设置cookie是设置值给浏览器的。因此我们需要通过response的对象来设置，设置cookie可以通过response.set_cookie来设置，这个方法的相关参数如下：

key：这个cookie的key。
value：这个cookie的value。
max_age：最长的生命周期。单位是秒。
expires：过期时间。跟max_age是类似的，只不过这个参数需要传递一个具体的日期，比如datetime或者是符合日期格式的字符串。如果同时设置了expires和max_age，那么将会使用expires的值作为过期时间。
path：对域名下哪个路径有效。默认是对域名下所有路径都有效。
domain：针对哪个域名有效。默认是针对主域名下都有效，如果只要针对某个子域名才有效，那么可以设置这个属性.
secure：是否是安全的，如果设置为True，那么只能在https协议下才可用。
httponly：默认是False。如果为True，那么在客户端不能通过JavaScript进行操作。
"""


def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2019, month=9, day=17, hour=23, minute=0, second=0)
    # 转为清醒时间
    expires = make_aware(expires)
    # 就算设置了max_age,也没有起效，最终还是会采用expires
    # 如果设置了path，就只能在该路径下访问
    # response.set_cookie('user_name', 'zhiliao', expires=expires, max_age=180, path='')
    response.set_cookie('user_id', 'abc', expires=expires, max_age=180, path='/cms/')
    return response


# 不在cms路径下无法得到user_id ,例如 path('list/', views.my_list)
def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)


# 在cms路径下访问
def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)


# 删除cookie：
def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('username')
    return response


def session_view(request):
    # 设置数据
    request.session['username'] = 'zhiliao'
    # 获取
    # username = request.session.get("username")
    # zhiliao
    # 删除数据
    # username = request.session.pop("username")
    # 删除之后再获取为空
    # username = request.session.get("username")
    # print(username)
    # None
    print("===================================")

    # 获取所有的键
    print(request.session.keys())
    # dict_keys(['username'])
    print("==================================")
    # 获取所有的键值对
    print(request.session.items())
    # dict_items([('username', 'zhiliao')])
    print(request.session.values())
    # dict_values(['zhiliao'])
    print("====================================")

    # clear：清除当前这个用户的session数据
    # request.session['password'] = "797439"

    # 删除session数据
    # request.session.clear()
    # password = request.session.get("password")
    # print(password)
    # None
    print("=====================================")

    # 删除数据库所有的数据,注销退出登录的时候用的比较多
    # 删除session并且删除在浏览器中存储的session_id
    # request.session.flush()

    """
    set_expiry(value)：设置过期时间。
    整形：代表秒数，表示多少秒后过期。
    0：代表只要浏览器关闭，session就会过期。
    None：会使用全局的session配置。在settings.py中可以设置SESSION_COOKIE_AGE来配置全局的过期时间。默认是1209600秒，也就是2周的时间。
    clear_expired：清除过期的session。Django并不会清除过期的session，需要定期手动的清理，或者是在终端，使用命令行
    python manage.py clearsessions来清除过期的session。
    """

    # 设置过期时间 -1代表已经过期
    request.session.set_expiry(-1)
    # 清除过期的session数据, 可以命令行运行命令
    # request.session.clear_expired()
    return HttpResponse("session view")
