from django.shortcuts import render

from .models import Category, Article, Tag
from django.http import HttpResponse
from frontuser import models


def index(request):
    # 要先存下父表数据才可以添加外键
    # category = Category(name="最新文章")
    # category.save()
    #
    # article = Article(title="abc", content="111")
    # article.category = category
    # article.save()

    # 查询
    # article = Article.objects.first()
    # print(article.title)  # abc
    # # 相当于多表连接查询，查询id下category中的name
    # print(article.category.name)
    # # 最新文章
    return HttpResponse('success')


# 外键级联删除，删除了父表中的id, 子表中也跟着删除
def delete_view(request):
    category = Category.objects.get(pk=2)
    category.delete()
    return HttpResponse("删除成功")


# 一对多表
def one_to_many_view(request):
    # 1.一对多的关联操作
    # article = Article(title='钢铁是怎么样练成的', content='abc')
    # category = Category.objects.first()  # 表示获取第一条记录
    # author = models.FrontUser.objects.first()  # 表示获取第一条记录
    # print(category)
    # print(author)
    # Category object (2)
    # FrontUser object (1)

    # article = Article(title='成功之路', content='abc')
    # category = Category.objects.get(pk=5)
    # author = models.FrontUser.objects.get(pk=2)
    #
    # article.category = category
    # article.author = author
    #
    # article.save()
    # 添加外键的的时候需要添加一条记录即可，不需要明确到id

    # article = Article.objects.get(pk=4)
    # # print(article)
    # # print(Article.objects.first())
    #
    # # print(article.frontuser.username) 这个是错误的表达
    # print(article.author.username)  # mike
    # return HttpResponse("success")

    # 2.获取某个分类下所有的文章
    # category = Category.objects.first()  # 第一个分类
    # article = category.article_set.first()  # 获取第一篇文章
    # category.article_set.all()     # 获取所有文章
    # <Article:(id:1, title:abc)>

    # 打印所有
    # articles = category.articles.all()
    # 可以使用另外一种模式设置好，在类里面直接设置好 related_name='articles'就不用这么麻烦
    # 例如：category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True,  related_name='articles')
    # for i in articles:
    #     print(i)
    # <Article:(id:1, title:abc)>
    # <Article:(id:2, title:钢铁是怎么样练成的)>

    # 另外一种添加方式
    # 通过某一个文章添加分类,注意当category_id可以为空的情况下才可以，如果为空就会报错
    # category = Category.objects.first()
    # article = Article(title='mmmmm', content='222')
    # article.author = models.FrontUser.objects.first()
    # article.save()
    # category.articles.add(article)
    # category.save()

    # 为了避免上面出现的错误，可以采取一下的方法
    category = Category.objects.first()
    article = Article(title='mmmmm', content='222')
    article1 = Article(title='mmmmm1', content='2221')
    article.author = models.FrontUser.objects.first()
    article1.author = models.FrontUser.objects.first()
    category.articles.add(article, article1, bulk=False)  # 可以添加多条记录
    category.save()
    return HttpResponse("success")


# 一对多
def one_to_one_view(request):
    # user = models.FrontUser.objects.first()
    # extension = models.UserExtension(school='知了')
    # extension.user = user
    # extension.save()

    # 通过信息打印作者
    extension = models.UserExtension.objects.first()
    print(extension.user)
    # <FrontUser:(id:1, username:外国人)>

    # 还可以通过作者来获取扩展信息
    user = models.FrontUser.objects.first()
    # 如果想简洁点可以通过设置relate_name参数来操作
    print(user.userextension)
    # <UserExtension:(id:1,school:知了, user_id:1)>
    return HttpResponse("success")


def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name='热门文章')
    # tag.save()
    # article.tag_set.add(tag)

    # 逆向添加
    # tag = Tag.objects.get(pk=1)
    # article = Article.objects.get(pk=6)
    # tag.articles.add(article)

    # 查看
    article = Article.objects.get(pk=4)
    tags = article.tag_set.all()
    for tag in tags:
        print(tag)
    # Tag object (1)
    # Tag object (2)

    tags = Tag.objects.get(pk=1)
    articles = tags.articles.all()
    for art in articles:
        print(art)
    # <Article:(id:4, title:成功之路)>
    # <Article:(id:6, title:财经之道)>
    return HttpResponse("success")
