from django.shortcuts import render
from django.shortcuts import render


def index(request):
    context = {
        "username": "谢茵茵"
    }
    return render(request, 'index.html', context=context)


def company(request):
    context = {
        "username": "吴铭明"
    }
    return render(request, 'company.html', context=context)


def school(request):
    return render(request, 'school.html')
