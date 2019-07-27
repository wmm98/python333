from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


# 第一种渲染模式
# def index(request):
#     html = render_to_string("index.html")  # 将模板渲染成字符串
#     return HttpResponse(html)


# 第二种渲染模式，更加简洁
def index(request):
    # html = render_to_string("index.html")
    return render(request, "index.html")
