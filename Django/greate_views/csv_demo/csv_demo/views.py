from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
import csv


# 小型的csv文件
def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=abc.csv"
    writer = csv.writer(response)
    writer.writerow(['username', 'age'])
    writer.writerow(['zhiliao', 18])
    return response


# 生成csv模板文件
def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=abc.csv"
    context = {
        'rows': [
            ['username', 'age'],
            ['zhiliao', 18]
        ]
    }

    # 获取模板
    template = loader.get_template('abc.txt')
    # 渲染模板
    csv_template = template.render(context)
    response.content = csv_template
    return response


# 生成大型的CSV文件
"""
SteamingHttpResponse,这个类是专门用来处理流数据的，使得在处理一些大型文件的时候，不会因为服务器处理时间长而导致连接超时
这个类不是继承HttpResponse,并且跟HttpResponse对比有一下几点区别

1.这个类没有属性content, 相反是streaming_content,这个类的streaming_content必须是一个可迭代对象，这个类没有write方法
，如果给这个类的对象写入数据会报错

注意：StreamingHttpResponse会启动一个进程来和客服端保持长连接，所以会很耗资源，说一如果不是特殊要求，尽量少用这种方法
"""


def large_csv_view(request):
    # response = StreamingHttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = "attachment;filename=large.csv"
    # response.streaming_content = ("username, age\n", "zhiliao, 18\n")

    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=large.csv"
    rows = ("Row {}, {}\n".format(row, row) for row in range(0, 10000))
    response.streaming_content = rows
    return response
