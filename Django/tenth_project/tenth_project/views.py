from django.shortcuts import render
from django.db import connection


def index(request):
    # 设游标
    cursor = connection.cursor()
    # 插入数据
    # cursor.execute("insert into book(id, name, author) values (null, '三国演义', '罗贯中')")
    cursor.execute("select * from book")
    # 返回一条数据
    # rows = cursor.fetchone()
    # 指定返回多少条数据,例如2条
    # rows = cursor.fetchmany(2)
    # 返回所有数据
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')
