from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def article(request):
    return HttpResponse("文章首页")


def article_list(request, categories):
    print('categories: %s' % categories)
    # categories: ['python', 'flask', 'django']
    print(reverse('list', kwargs={"categories": categories}))
    # /article/list/python+flask+django/
    text = "您填写的分类是 %s" % categories
    return HttpResponse(text)


def article_detail(request, article_id):
    # print(type(article_id))
    # return HttpResponse("文章详情 %s" % article_id)n
    # print(reverse('detail', kwargs={'article_id': article_id}))
    # # /article/detail/5/
    # print(type(article_id))
    # <class 'int'>
    return HttpResponse("文章详情")

# 自定义转换器
# 在‘文章分类’参数传到视图函数之前要把这些分类分开来存储到列表当中
# 不如参数‘python+django’,那么视图函数的时候就要变成‘[‘python’,‘django’]’。

# 以后在使用reverse反转的时候，限制传递“文章分类”参数应该是一个列表，而且要将这个列表变成'pyhton+django'的形式
