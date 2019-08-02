from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum
from django.db import connection
from front.models import Book, Author, BookOrder


def index(request):
    # 获取所有图书的定价的平均价
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # {'avg': 97.25}
    # 查看原生SQL语句
    print(connection.queries)
    # [{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.001'},
    #  {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.000'},
    #  {'sql': 'SELECT AVG(`book`.`price`) AS `avg` FROM `book`', 'time': '0.007'}]
    return HttpResponse("index")


def index2(request):
    # aggregate:返回使用聚合函数的后的字段和值
    # annotate:在原来模型字段的基础之上添加一个使用了聚合函数的字段，并且在使用聚合函数的时候
    #         会使用当前这个模型的主键进行分组（group by）

    # 获取每一本图书的平均价格
    result = Book.objects.annotate(avg=Avg("bookorder__price"))
    print(result)
    # <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>,
    # <Book: Book object (3)>, <Book: Book object (4)>]>
    print(connection.queries)
    """
    'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, ' \
    'AVG(`book_order`.`price`) AS `avg` FROM `book` LEFT OUTER JOIN `book_order` ON ' \
    '(`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id`
    """
    print("--------------------------")
    for book in result:
        print('%s/%s' % (book.name, book.avg))
    # 三国演义/89.33333333333333
    # 水浒传/93.5
    # 西游记/None
    # 红楼梦/None
    return HttpResponse("index2")


def index3(request):
    # book表中总共有多少本书
    result = Book.objects.aggregate(book_nums=Count("id"))
    print(result)
    # {'book_nums': 4}
    print(connection.queries)
    # 'SELECT COUNT(`book`.`id`) AS `book_nums` FROM `book`'

    # 查询作者表中总共有多少个不同的邮箱
    result1 = Author.objects.aggregate(email_nums=Count('email', distinct=True))
    print(result1)
    # {'email_nums': 3}
    print(connection.queries)
    # 'SELECT COUNT(DISTINCT `author`.`email`) AS `email_nums` FROM `author`'

    # 统计每本书的销量
    books = Book.objects.annotate(book_nums=Count("bookorder__id"))
    for book in books:
        print('%s/%s' % (book.name, book.book_nums))
        # 三国演义/3
        # 水浒传/2
        # 西游记/0
        # 红楼梦/0
    print(connection.queries)
    """
    'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`,' \
    ' `book`.`publisher_id`, COUNT(`book_order`.`id`) AS `book_nums` FROM `book` LEFT OUTER JOIN `book_order` ' \
    'ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` 
    """
    return HttpResponse("index3")


def index4(request):
    info = Author.objects.aggregate(max=Max("age"), min=Min("age"))
    print(info)
    # {'max': 46, 'min': 28}
    print(connection.queries)
    # SELECT MAX(`author`.`age`) AS `max`, MIN(`author`.`age`) AS `min` FROM `author

    # 查找每一本书售卖时候的最大价格以及最小价格
    books = Book.objects.annotate(max=Max("bookorder__price"), min=Min("bookorder__price"))
    for book in books:
        print("%s/%s/%s" % (book.name, book.max, book.min))
        # 三国演义/95.0/85.0
        # 水浒传/94.0/93.0
        # 西游记/None/None
        # 红楼梦/None/None
    print(connection.queries)
    """
    {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, 
    `book`.`publisher_id`, MAX(`book_order`.`price`) AS `max`, MIN(`book_order`.`price`) AS `min` FROM `book` 
    LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id`
    """
    return HttpResponse("index4")


def index5(request):
    # 求所有图书的销售总额
    result = BookOrder.objects.aggregate(total=Sum('price'))
    print(result)
    # {'total': 455.0}
    print(connection.queries)
    """'SELECT SUM(`book_order`.`price`) AS `total` FROM `book_order`'"""

    # 每一本图书的销售总额
    books = Book.objects.annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s/%s" % (book.name, book.total))
        # 三国演义/268.0
        # 水浒传/187.0
        # 西游记/None
        # 红楼梦/None
    print(connection.queries)
    """
    'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, 
    `book`.`publisher_id`, SUM(`book_order`.`price`) AS `total` FROM `book` LEFT OUTER JOIN `book_order` 
    ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id`
    """

    # 求2019年销售总额
    result = BookOrder.objects.filter(create_time__year=2019).aggregate(total=Sum('price'))
    print(result)
    # {'total': 360.0}
    # 求2018年度每一本图书的销售总额
    result = Book.objects.filter(bookorder__create_time__year=2019).annotate(total=Sum("bookorder__price"))
    print(result)
    print(connection.queries)
    """
    "SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, " \
    "`book`.`publisher_id`, SUM(`book_order`.`price`) AS `total` FROM `book` INNER JOIN `book_order` " \
    "ON (`book`.`id` = `book_order`.`book_id`) WHERE `book_order`.`create_time` BETWEEN '2019-01-01 00:00:00' " \
    "AND '2019-12-31 23:59:59.999999' GROUP BY `book`.`id`
    """
    for i in result:
        print("%s%s" % (i.name, i.total))
        # 三国演义173.0
        # 水浒传187.0
    return HttpResponse("index5")