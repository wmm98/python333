from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'value': '你好',
        # 构造时间
        'my_time': datetime(year=2019, month=7, day=22, hour=16, minute=12, second=0)
    }
    return render(request, 'index.html', context=context)
