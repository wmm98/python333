from django.shortcuts import render
from django.db import connection


# 场景一
# 实现一个根据用户id获取用户详情的视图。示例代码如下：
def index(request):
    # http://127.0.0.1:8000/?user_id=1
    user_id = request.GET.get("user_id")
    # 如果是传入 http://127.0.0.1:8000/?user_id=1 or 1=1就会打印所有的信息，因为1=1永远满足条件，返回数据库中全部的信息

    context = {}
    if user_id:
        cursor = connection.cursor()
        cursor.execute("select id, username from front_user where id=%s" % user_id)
        rows = cursor.fetchall()
        context['rows'] = rows
    return render(request, 'index.html', context=context)


# 场景二：
# 实现一个根据用户的username提取用户的视图。示例代码如下：
def index1(request):
    username = request.GET.get("username")
    # 原理和id一样
    # http://127.0.0.1:8000/index1/?username= ’小明‘or ‘1=2‘
    context = {}
    if username:
        cursor = connection.cursor()
        # 预防
        sql = "select id, username from front_user where username=%s"
        cursor.execute(sql, (username, ))
        # cursor.execute("select id, username from front_user where username=%s" % username)
        rows = cursor.fetchall()
        context['rows'] = rows
    return render(request, 'index1.html', context=context)

"""

永远不要信任用户的输入。对用户的输入进行校验，可以通过正则表达式，或限制长度；对单引号和 双"-"进行转换等。
永远不要使用动态拼装sql，可以使用参数化的sql或者直接使用存储过程进行数据查询存取。比如：

永远不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接。
不要把机密信息直接存放，加密或者hash掉密码和敏感的信息。
应用的异常信息应该给出尽可能少的提示，最好使用自定义的错误信息对原始错误信息进行包装。

在Django中如何防御sql注入：
使用ORM来做数据的增删改查。因为ORM使用的是参数化的形式执行sql语句的。
如果万一要执行原生sql语句，那么建议不要拼接sql，而是使用参数化的形式。

"""