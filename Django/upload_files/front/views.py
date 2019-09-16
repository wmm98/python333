from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    # 上传文件
    # def post(self, request):
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     file = request.FILES.get("myfile")
    #     Article.objects.create(title=title, content=content, thumbnial=file)
    #     return HttpResponse("成功")

    # 上传限制扩展名文件
    # 这个时候的前端代码字段名要和表单的一样
    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("成功")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("失败")
