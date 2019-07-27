from django.shortcuts import render
from datetime import datetime


# DTL常用过滤器1,最多只能有两个参数
# cut 相当与python中的repalce
# add 相当于pyhton中数字的相加或其他类型的拼接

def greet():
    return 'hello'


def index(request):
    context = {
        'greet': greet  # 调用greet函数
    }
    return render(request, 'index.html', context=context)


# 数字和字符串的拼接都可以，数字先转为int类型
def add_view(request):
    return render(request, 'add.html')


# 列表元组拼接不能直接传参
def add_list(request):
    context = {
        'value1': (1, 2, 5, 7),
        'value2': (2, 9, 0)
    }
    return render(request, 'add_list.html', context=context)


# cut过滤器
def cut_view(request):
    return render(request, 'cut.html')


# date 过滤器
def date_view(request):
    context = {
        "today": datetime.now()
    }
    return render(request, 'date.html', context=context)


# default 如果值被评估为false, 比如[],"", None, {}等这些在if判断中为False的值，都会使用default过滤器提供的默认值
# 如果value是等于一个空的字符串， 比如"",那么以上代码将会输出nothing

# default_if_none,如果值是none,那么将会使用default_if_none提供的默认值，这个和default有区别，default是所有被评估为False的都会
# 使用默认值，而default_if_none则只有这个值等于None的时候才会使用默认值

def default_view(request):
    context = {
        # 'value': 'hello'
        'value': None
    }
    return render(request, 'default.html', context=context)


# 取第一个和最后一个值
def first_last_view(request):
    context = {
        'value': ['a', 'b', 'c', 'd']
    }
    return render(request, 'first.html', context=context)


# floatformat使用四舍五入的方式格式化一个浮点类型，如果这个过滤器没有传递任何参数，那么只会在小数点后保留一个小数，如果小数后面是0
# 那么只会保留整数，当然也可以传递一个参数，标识具体要保留几个小数
# 例如： {{ value|floatformat }}  传参数 {{ value|flaotformat:3}} 保留3位小数

def floatformat_view(request):
    context = {
        'value': 78.985
    }
    return render(request, 'floatformat_view.html', context=context)


# jion类似python中的join, 将列表/元组/字符串用指定的字符进行拼接
# 例如 {{ value|join:"/"}}
def join_view(request):
    context = {
        'value': [1, 2, 3]
    }
    return render(request, 'join_view.html', context=context)


# length获取一个列表/字符串/字典的长度（在join_views函数实现）
# 例如{{ value|length }},如果value的值为None,那么以上将的那会0


# lower,upper同python用法
def lower(request):
    context = {
        'value': "HKDHASIOhi hi"
    }
    return render(request, 'lower.html', context=context)


# random在被给的列表/字符串/元组中随机选择一个值
# 例如 {{ value|random }}
def random_view(request):
    context = {
        'value': [1, 3, 5, 3, 9]
    }
    return render(request, 'random_view.html', context=context)


# safe 标志这个字符串是安全的，也即会关掉这个字符串的自动转义
# 例如 {{ value|safe }}
# 如果value是一个不含任何特殊字符的字符串，不如<a>这种，那么以上代码就会把字符串正常输入
# 如果value是一串html代码，那么以上代码就会把这个html渲染到浏览器中
def safe_view(request):
    context = {
        'value': "<script>alert('hello world');</script>"
    }
    return render(request, 'safe_view.html', context=context)


# slice 类似于pyhton的切片操作， 例如： {{ some_list|slice:"2:" }}表示代码会给some_list从2开始做切片操作
def slice_view(request):
    context = {
        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 40]
    }
    return render(request, 'slice_view.html', context=context)


# stringtags 删除字符串中所有的html标签 例如 {{ value|stringtags }}
# 如果value是<strong>hello world</strong>,那么以上代码将会输出hello word
def striptags_view(request):
    context = {
        'value': '<script>alert("hello world")</script>'
    }
    return render(request, 'striptags_view.html', context=context)


# truncatechars 如果给定的字符串长度超过了过滤器指定的长度，那么就会进行切割，并且会拼接三个点作为省略号
# 例如： {{ value|truncatechars }}
# 如果value是等于 北京欢迎你 ，那么输出的结果是 北京... ，北京+... 的长度就是5
def truncatechars_view(request):
    context = {
        'value': '北京欢迎你@@@@'
    }
    return render(request, 'truncatechars_view.html', context=context)


# 类似于truncatechars, 只不过是不会切割html标签，例如： {{ value|truncatechars_html:5}}
# 如果value是等于<p>北京欢迎你<p>, 那么输出的字符是<p>北京...<p>
def truncatechars_html_view(request):
    context = {
        'value': '<p>北京欢迎你@@@@</p>'
    }
    return render(request, 'truncatechars_html_view.html', context=context)
