from django.shortcuts import render


# 在子模引入父模板的时候可以传入参数
# 子模版使用的时候也可以手动传
def index(request):
    context = {
        'username': 'zhiliao'
    }
    return render(request, 'index.html', context=context)


def company(request):
    return render(request, 'company.html')


def school(request):
    return render(request, 'school.html')
