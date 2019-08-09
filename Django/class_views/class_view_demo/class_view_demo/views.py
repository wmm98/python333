from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse('index')


class BookListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("BookListView")


class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_book.html')

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get("name")
        book_author = request.POST.get("author")
        print("name:{},author:{}".format(book_name, book_author))
        # name:偷影子的人,author:马克李维
        return HttpResponse("success")


class BookDetail(View):
    # 传入参数book_id
    def get(self, request, book_id):
        content = "图书的id是： %s" % book_id
        return HttpResponse(content)

    def dispatch(self, request, *args, **kwargs):
        print('调用get方法之前先调用dispatch方法')
        return super(BookDetail, self).dispatch(request, *args, **kwargs)

    # 类视图只有get方法的时候，用其他方法请求会出错，那么可以以下方法来提醒
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持get以外的其他请求")


class AboutView(TemplateView):
    template_name = 'AboutView.html'

    def get_context_data(self, **kwargs):
        # 会将该参数传递到AboutView.html
        context = {"phone": "17765602533"}
        return context
