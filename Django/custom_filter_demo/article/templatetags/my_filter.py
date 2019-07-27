# 自定义模板过滤器，模板过滤器必须要放在app中，并且这个app必须要要在INSTALLED_APPS中进行安装，然后再在这个
# app下面创建一个python包叫做templatetags.再在这个包下面创建一个python文件

# 在创建了存储过滤器的文件后，接下来就是在这个文件中写过滤器了。过滤器实际上就是python中的一个函数，只不过是把这个函数注册到模板库中，
# 以后在模板中就可以使用到这个函数了。但是这个函数有参数限制，第一个参数必须是这个过滤器需要处理的值，第二个参数可有可无，如果有，那么意味着
# 在模板中可以传递参数。并且过滤器的参数最多只有2个，在写完过滤器后，再使用django.templates.Library对象注册进去，例如：

from django import template
from datetime import datetime

register = template.Library()


# 过滤器嘴都只能有两个参数
# 过滤器的第一个参数永远都是被过滤的那个参数（也就是竖线左边那个参数）
@register.filter
def greet(value, word):
    return value + word


@register.filter
def time_since(value):
    """
   time距离现在的时间间隔
   1.如果时间间隔小于1分钟以前，那么就显示"刚刚"
   2.如果大于1分钟小于1小时， 那么就显示"xx分钟前"
   3.如果是大于1小时小于24小时，那么就显示"xxx小时前"
   4.如果是大于24小时小于30天以内，那么就显示"xx天前"
   5.否则就显示具体时间
   2019/10/20
   16:15
   """
    if not isinstance(value, datetime):
        return value
    now = datetime.now()
    # timedeplay.total.seconds 获取秒
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return "刚刚"
    elif 60 <= timestamp < 60*60:
        minutes = int(timestamp/60)
        return '%s分钟前' % minutes
    elif 60*60 <= timestamp < 60*60*24:
        hours = int(timestamp/60/60)
        return '%s小时前' % hours
    elif 60*60*24 <= timestamp < 60*60*30:
        days = int(timestamp/60/60/24)
        return '%s小时前' % days
    else:
        return value.strftime("%Y/%m/%d %H:%M")  # 返回当前时间


# register.filter("greet", greet) 相当于@register.filter
# # 第一个greet代表定义过滤器的名字，第二个代表过滤器对应的函数
