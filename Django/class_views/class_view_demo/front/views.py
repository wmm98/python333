from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Article
from django.views.generic import ListView, View
from django.core.paginator import Paginator, Page
from django.utils.decorators import method_decorator


def add_article(request):
    articles = []
    for i in range(0, 102):
        article = Article(title="标题：%s" % i, content="内容： %s" % i)
        articles.append(article)
    # 批量插入数据
    Article.objects.bulk_create(articles)
    return HttpResponse("数据添加成功")


"""
首先ArticleListView是继承自ListView。
model：重写model类属性，指定这个列表是给哪个模型的。
template_name：指定这个列表的模板。
paginate_by：指定这个列表一页中展示多少条数据。
context_object_name：指定这个列表模型在模板中的参数名称。
ordering：指定这个列表的排序方式。
page_kwarg：获取第几页的数据的参数名称。默认是page。
get_context_data：获取上下文的数据。
get_queryset：如果你提取数据的时候，并不是要把所有数据都返回，那么你可以重写这个方法。将一些不需要展示的数据给过滤掉。
"""


class article_list(ListView):
    model = Article
    template_name = 'article_list1.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(article_list, self).get_context_data(*kwargs)
        context['username'] = 'zhiliao'
        print("===============================================")
        print(context)
        """
        {'paginator': <django.core.paginator.Paginator object at 0x000001E28B42F160>, 'page_obj': <Page 2 of 11>,
         'is_paginated': True, 'object_list': <QuerySet [<Article: Article object (11)>, <Article: Article object (12)>, 
         <Article: Article object (13)>, <Article: Article object (14)>, <Article: Article object (15)>, 
         <Article: Article object (16)>, <Article: Article object (17)>, <Article: Article object (18)>,
          <Article: Article object (19)>, <Article: Article object (20)>]>, 'articles': <QuerySet [<Article: Article object (11)>,
           <Article: Article object (12)>, <Article: Article object (13)>, <Article: Article object (14)>, 
           <Article: Article object (15)>, <Article: Article object (16)>, <Article: Article object (17)>, 
           <Article: Article object (18)>, <Article: Article object (19)>, <Article: Article object (20)>]>, 
           'view': <front.views.ArticleListView object at 0x000001E28B42F780>, 'username': 'zhiliao'}
        """
        print("==============================================")

        # 调用get_pagination_data函数
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    # get_queryset：如果你提取数据的时候，并不是要把所有数据都返回，那么你可以重写这个方法。将一些不需要展示的数据给过滤掉。
    # def get_queryset(self):
    #     # 只显示前面9条数据
    #     return Article.objects.filter(id__lte=9)

    # 默认around_count=2
    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        # 总页数
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_pages': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }


# 装饰器
def login_required(func):
    def wrapper(request, *args, **kwargs):
        # ?username=zhiliao
        username = request.GET.get('username')
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('front:login'))
    return wrapper


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("个人中心界面")

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView, self).dispatch(request, *args, **kwargs)


def login(request):
    return HttpResponse('login')