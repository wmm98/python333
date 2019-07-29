from django.http import HttpResponse
from .models import Article, Category
from datetime import datetime, time
from django.utils.timezone import make_aware


def index(request):
    # exact 等价于sql中where

    article = Article.objects.filter(title__exact="中国高铁")
    print(article.query)  # 打印原生sql语句
    print(article)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` = 中国高铁
    # <QuerySet [<Article: Article object (2)>]>

    # iexact 等价于模糊查询中的like，查找的对象要完全等价才可以
    article = Article.objects.filter(content__iexact="高铁")
    print(article.query)
    print(article)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`content` LIKE 高铁
    # <QuerySet [<Article: Article object (1)>]>
    return HttpResponse("成功！！！")


def index1(request):
    # contains 只要包含'铁'都会查询出来
    # icontains 跟contains用法差不多，只是icontains对大小写不敏感
    result = Article.objects.filter(title__contains='铁')
    print(result.query)
    print(result)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE BINARY %铁%
    # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
    return HttpResponse("成功")


def index2(request):
    # 查找id 在1,2,3里面的的文章
    # articles = Article.objects.filter(id__in=[1, 2, 3])
    # for article in articles:
    #     print(article)

    # 查找文章id 为3，4的文章分类
    categories = Category.objects.filter(article__id__in=[3, 4])
    for category in categories:
        print(category)
        # Category object (1)
        # Category object (3)

    # 所有文章包含hello的分类
    categories1 = Category.objects.filter(article__title__contains='hello')
    for category1 in categories1:
        print(category1)
    # Category object (2)
    # Category object (3)
    return HttpResponse("成功")


def index3(request):
    # 查找id大于2的左右文章
    # gt:greater than
    # gte: greater than equal
    articles = Article.objects.filter(id__gt=2)
    print(articles)
    # <QuerySet [<Article: Article object (3)>, <Article: Article object (4)>]>
    print(articles.query)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`
    # FROM `article` WHERE `article`.`id` > 2

    # 查找小于2的左右文章
    # lte 小于等于
    articles = Article.objects.filter(id__lt=2)
    print(articles)
    print(articles.query)
    # <QuerySet [<Article: Article object (1)>]>
    # SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`id` < 2
    return HttpResponse("成功")


def index4(request):
    # startwith 以什么开头 区分大小写
    # istartswith 不区分大小写
    # endswith 以什么结尾
    # articles = Article.objects.filter(title__startswith="中国")
    # print(articles)
    # print(articles.query)
    # <QuerySet [<Article: Article object (2)>]>
    # SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`title` LIKE BINARY 中国%

    articles = Article.objects.filter(title__endswith="hello")
    for i in articles:
        print(i)
    # print(articles)
    return HttpResponse("成功")


def index5(request):
    # range可以指定一个时间段并且时间段标记为"aware",要不django会报出警告
    # 相当于sql中的between
    start_time = make_aware(datetime(year=2019, month=7, day=27, hour=6, minute=35, second=31))
    end_time = make_aware(datetime(year=2019, month=7, day=28, hour=6, minute=35, second=31))
    articles = Article.objects.filter(create_time__range=(start_time, end_time))
    print(articles.query)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time`
    # FROM `article` WHERE `article`.`create_time` BETWEEN 2019-07-26 22:35:31 AND 2019-07-27 22:35:31
    print(articles)
    # `article` WHERE `article`.`create_time` BETWEEN 2019-07-26 22:35:31 AND 2019-07-27 22:35:31
    # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>,
    # <Article: Article object (3)>, <Article: Article object (4)>, <Article: Article object (5)>,
    # <Article: Article object (6)>]>
    return HttpResponse("成功")


def index6(request):
    # 查找日期为2019/7/27的文章信息
    # articles = Article.objects.filter(create_time__date=datetime(year=2019, month=7, day=27))

    # 查找文章年份为2019的
    # articles = Article.objects.filter(create_time__year=2019)

    # 查找文章年份大于2019年的
    # articles = Article.objects.filter(create_time__year__gte=2019)

    # 其中year和month还有day的用法一样的

    # print(articles.query)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time`
    # FROM `article` WHERE DATE(CONVERT_TZ(`article`.`create_time`, 'UTC', 'Asia/Shanghai')) = 2019-07-27

    # print(articles)
    # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>,
    # <Article: Article object (3)>, <Article: Article object (4)>, <Article: Article object (5)>,
    # <Article: Article object (6)>]>

    # 查找星期几的week_day: 星期一到星期天的表示[2, 3, 4, 5, 6, 7, 1]
    # articles = Article.objects.filter(create_time__week_day=4)

    # time
    # 查找时间time,需要加上8个小时，数据库存的是东八区时间
    # 查找在6：35：31到6:25:32之间的信息

    # time是import datetime里的time
    start_time = time(hour=14, minute=35, second=31)
    end_time = time(hour=14, minute=35, second=32)
    articles = Article.objects.filter(create_time__time__range=(start_time, end_time))
    print(articles)
    # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>,
    # <Article: Article object (3)>, <Article: Article object (4)>, <Article: Article object (5)>,
    # <Article: Article object (6)>]>

    return HttpResponse("成功")


# isnull, regex
def index7(request):
    # 查询为空文章，False不为空
    articles = Article.objects.filter(create_time__isnull=True)
    print(articles)
    # <QuerySet [<Article: Article object (1)>]>

    # 使用正则表达式查询
    # 查询以hello开头的文章
    # iregex不区分大小写
    articles = Article.objects.filter(title__regex=r"^我")
    print(articles)
    # <QuerySet [<Article: Article object (4)>, <Article: Article object (5)>]>
    return HttpResponse("成功")
