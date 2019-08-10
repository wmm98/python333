from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
from django.http import HttpResponse
from django.forms.utils import ErrorDict


class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context={'form': form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')

            print('=========================================')
            print(title)
            print(content)
            print(email)
            print(reply)
            # ffff
            # dsdsafdsa
            # jfkdsj@qq.com
            # True
            print("===========================================")
            return HttpResponse("success")
        else:
            print(print(form.get_json_data()))
            # {'title': [{'message': '最少不能少于1个字符', 'code': 'min_length'}],
            #  'content': [{'message': '必须要传content字段', 'code': 'required'}],
            #  'email': [{'message': '必须要传eamil字段!', 'code': 'required'}]}
            # <class 'django.forms.utils.ErrorDict'>
            return HttpResponse("fail")


# class IndexView(View):
#     def get(self, request):
#         form = MessageBoardForm()
#         return render(request, 'index.html', context={'form': form})
#
#     def post(self, request):
#         form = MessageBoardForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             email = form.cleaned_data.get('email')
#             reply = form.cleaned_data.get('reply')
#             print("=====================================")
#             print(title)
#             print(content)
#             print(email)
#             print(reply)
#             print("=====================================")
#             return HttpResponse('success')
#         else:
#             print(form.errors)
#             return HttpResponse('fail')
