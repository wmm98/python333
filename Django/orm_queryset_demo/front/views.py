from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum, F, Q, Prefetch
from django.db import connection
from front.models import Book, Author, BookOrder, Publisher


def index(request):
    print(type(Book.objects))
    # <class 'django.db.models.manager.Manager'>
    return HttpResponse("index")


def index2(request):
    # 链式调用
    # id >= 2且id !=3的数据
    # books = Book.objects.filter(id__gte=2).filter(~Q(id=3))
    # exclude去除满足条件的数据
    # 用法等用上一条语句
    books = Book.objects.filter(id__gte=2).exclude(id=3)
    for book in books:
        print(book)
        # Book object (2)
        # Book object (4)
    print("----------------------------------------------------")
    # 查找书本信息以及作者
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        print("%s %s" % (book.name, book.author_name))
        # 三国演义 罗贯中
        # 水浒传 施耐庵
        # 西游记 吴承恩
        # 红楼梦 sna@qq.com
    print(connection.queries[-1])
    """ 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.
    `publisher_id`, `author`.`name` AS `author_name` FROM `book` INNER JOIN `author` ON (`book`.`author_id` = `author`.`id`)"""
    return HttpResponse("index2")


# order by的使用
def index3(request):
    # 1. 根据create_time从小到大排序
    # orders = BookOrder.objects.order_by("create_time")
    # 2. 根据create_time从大到小排序
    # orders = BookOrder.objects.order_by("-create_time")
    # 3.首先根据create_time从大到小排序，如果create_time是一样的，那么根据price从小到大排序
    # orders = BookOrder.objects.order_by("-create_time", '-price')
    # 不等同于上面语句
    # orders = BookOrder.objects.order_by("-create_time").order_by("price")
    # 4.根据订单的图书的评分来进行排序(从小到大)
    orders = BookOrder.objects.order_by("book__rating")
    for order in orders:
        print("%s %s" % (order.id, order.book.rating))
    print(connection.queries)
    '''
    'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` ' \
    'INNER JOIN `book` ON (`book_order`.`book_id` = `book`.`id`) ORDER BY `book`.`rating` ASC'
    '''
    print("-------------------------------------------------------------------------------")

    # 5.根据图书数据，根据图书的销量进行排序（从大到小进行排序）
    books = Book.objects.annotate(order_nums=Count("bookorder")).order_by("-order_nums")
    for book in books:
        print("%s %s" % (book.name, book.order_nums))
        # 三国演义 3
        # 水浒传 2
        # 红楼梦 0
        # 西游记 0
    print(connection.queries[-1])
    '''
    'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, ' \
    'COUNT(`book_order`.`id`) AS `order_nums` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) ' \
    'GROUP BY `book`.`id` ORDER BY `order_nums` DESC'
    '''

    # 排序也可以在models里Metal类里面直接设置好，查询的时候直接按照此排序

    return HttpResponse("index3")


def index4(request):
    # books = Book.objects.annotate(author_name=F("author__name"))
    # for book in books:
    #     print(book.name, book.author_name)
    # return HttpResponse("index4")

    # value可以只提取需求得字段
    # books = Book.objects.values('id', "name", "author__name")
    # 如果另起名字
    books = Book.objects.values('id', "name", writer=F("author__name"))
    print(type(books))
    # <class 'django.db.models.query.QuerySet'>
    for book in books:
        print(book)
        # {'id': 1, 'name': '三国演义', 'writer': '罗贯中'}
        # {'id': 2, 'name': '水浒传', 'writer': '施耐庵'}
        # {'id': 3, 'name': '西游记', 'writer': '吴承恩'}
        # {'id': 4, 'name': '红楼梦', 'writer': 'sna@qq.com'}

    print("-----------------------------------------")
    # 查询书得销售量
    books = Book.objects.values('id', 'name', order_nums=Count("bookorder__id"))
    for book in books:
        print(book)
        # {'id': 1, 'name': '三国演义', 'order_nums': 3}
        # {'id': 2, 'name': '水浒传', 'order_nums': 2}
        # {'id': 3, 'name': '西游记', 'order_nums': 0}
        # {'id': 4, 'name': '红楼梦', 'order_nums': 0}

    print("-------------------------------------------")
    # 当不传任何参数得时候
    books = Book.objects.values()
    for book in books:
        print(book)
        # {'id': 1, 'name': '三国演义', 'pages': 987, 'price': 148.0, 'rating': 4.8, 'author_id': 3, 'publisher_id': 1}
        # {'id': 2, 'name': '水浒传', 'pages': 967, 'price': 147.0, 'rating': 4.83, 'author_id': 4, 'publisher_id': 1}
        # {'id': 3, 'name': '西游记', 'pages': 1004, 'price': 145.0, 'rating': 4.85, 'author_id': 2, 'publisher_id': 2}
        # {'id': 4, 'name': '红楼梦', 'pages': 1007, 'price': 90.0, 'rating': 4.9, 'author_id': 1, 'publisher_id': 2}
    print("-----------------------------------------------")

    books = Book.objects.values_list()
    for book in books:
        print(book)
        # (1, '三国演义', 987, 148.0, 4.8, 3, 1)
        # (2, '水浒传', 967, 147.0, 4.83, 4, 1)
        # (3, '西游记', 1004, 145.0, 4.85, 2, 2)
        # (4, '红楼梦', 1007, 90.0, 4.9, 1, 2)
    print("--------------------------------------------------")

    # 当values_list只提取一个字段时
    books = Book.objects.values_list('name', flat=True)
    for book in books:
        print(book)
        # 三国演义
        # 水浒传
        # 西游记
        # 红楼梦
    return HttpResponse("index4")


def index5(request):
    """
    select_relate :在查找某个表的数据的时候，可以一次性地把相关联的其他表的数据都提取出来，这样
    可以在以后访问相关联的表的数据的时候，不用再次查找数据库，可以节省一些开销,注意这个方法只能用在外键的关联对象上
    对于那种多对对，或者多对一的情况，不能使用他来实现，而应该使用‘perfect_related来实现’
    """
    # books = Book.objects.all()
    # # for book in books:
    # #     print(book)
    # print(connection.queries)

    books = Book.objects.select_related("author", 'publisher')
    print(type(books))
    # <class 'django.db.models.query.QuerySet'>
    # 该语句只执行一次查询
    for book in books:
        print(book.author.name, " ", book.publisher.name)
        # 罗贯中   新华出版社
        # 施耐庵   新华出版社
        # 吴承恩   东动软出版社
        # sna@qq.com   东动软出版社
    print(connection.queries)
    """
        {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, '
            '`book`.`publisher_id`, `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email`, `publisher`.`id`, '
            '`publisher`.`name` FROM `book` INNER JOIN `author` ON (`book`.`author_id` = `author`.`id`) INNER JOIN '
            '`publisher` ON (`book`.`publisher_id` = `publisher`.`id`)'
    """
    print("------------------------------------------------------------")

    # 下面的是错的，因为book没有直接关联bookorder表
    # books = Book.objects.select_related('bookorder')
    # for book in books:
    #     print(book)
    # Invalid field name(s) given in select_related: 'bookorder'. Choices are: author, publisher

    print("-----------------------------------------")
    return HttpResponse("index5")


def index6(request):
    # # 原始方法
    # # books = Book.objects.all()
    # # for book in books:
    # #     print("-" * 40)
    # #     print(book.name)
    # #     orders = book.bookorder_set.all()
    # #     for order in orders:
    # #         print(order.id)
    #     # ----------------------------------------
    #     # 三国演义
    #     # 1
    #     # 2
    #     # 3
    #     # ----------------------------------------
    #     # 水浒传
    #     # 4
    #     # 5
    #     # ----------------------------------------
    #     # 西游记
    #     # ----------------------------------------
    #     # 红楼梦
    # # print(connection.queries)
    # # 按照这样的方法会产生很多的查询语句，效率低下
    # #  {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.004'},
    # # {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE `book_order`.`book_id` = 1', 'time': '0.003'},
    # #  {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE `book_order`.`book_id` = 2', 'time': '0.000'},
    # #  {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE `book_order`.`book_id` = 3', 'time': '0.000'},
    # #  {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE `book_order`.`book_id` = 4', 'time': '0.001'}
    #
    # print("*" * 40)
    # # 优化，此方法一对一，一对多，多对多都适合用，只不过要发生两次查询，如果一对多一对一的关系最好用select_realted
    # # 只会产生一次查询
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("-" * 40)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # print(connection.queries)
    # """
    # {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.001'},
    # {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE `book_order`.`book_id` IN (1, 2, 3, 4)'
    # """
    #
    # print("-------------------------")
    # # 查找外键关联的也可以，产生两次查询
    # books1 = Book.objects.prefetch_related("author")
    # for book1 in books1:
    #     print(book1.name, book1.author.name)
    #     # 三国演义 罗贯中
    #     # 水浒传 施耐庵
    #     # 西游记 吴承恩
    #     # 红楼梦 sna@qq.com
    # print(connection.queries)
    # """
    # {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.000'}
    # {'sql': 'SELECT `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email` FROM `author` WHERE `author`.`id` IN (1, 2, 3, 4)'
    # """
    # print("-----------------------------------------------")
    # # 注意事项：
    # # 现在有一个新需求，要过滤价格大于88的图书
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("-" * 40)
    #     print(book.name)
    #     orders = book.bookorder_set.filter(price__gt=88)
    #     for order in orders:
    #         print(order.id)
    # print(connection.queries)
    # """[{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.000'}, {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
    #  'time': '0.000'}, {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.
    #  `author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.001'}, {'sql': 'SELECT VERSION()', 'time': '0.000'},
    #  {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time`
    #  FROM `book_order` WHERE `book_order`.`book_id` IN (1, 2, 3, 4)', 'time': '0.001'}, {'sql': 'SELECT `book_order`.`id`,
    #  `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order`
    #  WHERE (`book_order`.`book_id` = 1 AND `book_order`.`price` > 88.0e0)', 'time': '0.001'},
    #   {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time`
    #   FROM `book_order` WHERE (`book_order`.`book_id` = 2 AND `book_order`.`price` > 88.0e0)', 'time': '0.001'},
    #   {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time`
    #   FROM `book_order` WHERE (`book_order`.`book_id` = 3 AND `book_order`.`price` > 88.0e0)', 'time': '0.001'},
    #   {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time`
    #   FROM `book_order` WHERE (`book_order`.`book_id` = 4 AND `book_order`.`price` > 88.0e0)', 'time': '0.000'}]"""
    # # 这样的话产生的查询就跟原始的查询一样多，prefetch_related就不起作用了

    print("----------------------------------------------------------------------")

    # 优化代码
    prefetch = Prefetch("bookorder_set", queryset=BookOrder.objects.filter(price__gt=88))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print("-" * 40)
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
            # ----------------------------------------
            # 三国演义
            # 1
            # ----------------------------------------
            # 水浒传
            # 4
            # 5
            # ------------------------------------- ---
            # 西游记
            # ----------------------------------------
            # 红楼梦
    print(connection.queries)
    # 只产生两次查询
    """
    {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`},\
    {'sql': 'SELECT `book_order`.`id`, `book_order`.`book_id`, `book_order`.`price`, `book_order`.`create_time` FROM `book_order` WHERE (`book_order`.`price` > 88.0e0 AND `book_order`.`book_id` IN (1, 2, 3, 4))'}
    """
    return HttpResponse("index6")


# defer and only
def index7(request):
    # 过滤掉name字段
    # books = Book.objects.defer("name")
    # """
    # 'SELECT `book`.`id`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`'
    # """
    # # 但是还是可以查询到name字段，只是每循环一遍book就要查询一遍，消耗大。
    # for book in books:
    #     print(book.name)
    # print(connection.queries)

    print("-----------------------------------------")
    # 只查询name字段，但过滤不掉id字段
    books = Book.objects.only('name')
    for book in books:
        print(book.id, book.name)
        # 1 三国演义
        # 2 水浒传
        # 3 西游记
        # 4 红楼梦
    print(connection.queries)
    # 'sql': 'SELECT `book`.`id`, `book`.`name` FROM `book`'
    return HttpResponse("index7")


# get方法，该方法只能匹配到一条数据，如果返回多条则会报错，如果不返回数据也会报错
def index8(request):
    # book = Book.objects.get(id__gt=2)
    # get() returned more than one Book -- it returned 2!
    book = Book.objects.get(id=2)
    print(type(book))
    # <class 'front.models.Book'>
    print(connection.queries)
    """
    'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.
    `author_id`, `book`.`publisher_id` FROM `book` WHERE `book`.`id` = 2'
    """
    return HttpResponse("index8")


def index9(request):
    # 插入数据
    # 原本方法
    # publisher = Publisher(name='知了课堂')
    # publisher.save()

    # 新方法
    publisher = Publisher.objects.create(name="知了上课")
    print(connection.queries)
    # INSERT INTO `publisher` (`name`) VALUES ('知了上课')"
    return HttpResponse("index9")


def index10(request):
    # get_or_create表示获取数据，如果没有该数据就创建
    result = Publisher.objects.get_or_create(name='知了出版社')
    print(result)
    # (<Publisher: Publisher object (5)>, True)表示创建
    print(result[0])
    # Publisher object (5)

    # 多条数据插入
    publisher = Publisher.objects.bulk_create([
        Publisher(name='123出版社'),
        Publisher(name='abc出版社')
    ])
    print(connection.queries)
    return HttpResponse("index10")


def index11(request):
    # len为python的，相对于比较低效
    # books = Book.objects.all()
    # print(len(books)) 4
    # print(connection.queries)

    # count为数据库层面的，比较高效
    # count = Book.objects.count()
    # print(count)
    # print(connection.queries)
    # # 'sql': 'SELECT COUNT(*) AS `__count` FROM `book`
    #
    # print("----------------------------------------")
    #
    # # exit
    # result = Book.objects.filter(name='三国演义').exists()
    # print(result)
    # # True
    # print(connection.queries)
    # # 'sql': "SELECT (1) AS `a` FROM `book` WHERE `book`.`name` = '三国演义'

    print("------------------------------------")

    # 比count更高效
    if Book.objects.filter(name='三国演义').count() > 0:
        print(True)
    print(connection.queries)
    # {'sql': "SELECT COUNT(*) AS `__count` FROM `book` WHERE `book`.`name` = '三国演义'"

    print("---------------------------------------")
    # 也比直接判断QuerySet更高效
    if Book.objects.filter(name='三国演义'):
        print(True)
    print(connection.queries)
    # 'sql': "SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`," \
    #        " `book`.`publisher_id` FROM `book` WHERE `book`.`name` = '三国演义'", 'time': '0.001'}]
    return HttpResponse("index11")


def index12(request):
    # 过滤掉重复的数据
    # 打印销售价格大于80块钱的书本
    # books = Book.objects.filter(bookorder__price__gte=80).distinct()
    # for book in books:
    #     print(book)
    #     # Book object (1)
    #     # Book object (2)
    # print(connection.queries)
    """
    'SELECT DISTINCT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, ' \
    '`book`.`publisher_id` FROM `book` INNER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) ' \
    'WHERE `book_order`.`price` >= 80.0e0'
    """

    # 如果将销售价格作为一个字段，信息会完全不一样
    # result = Book.objects.annotate(order_price=F("bookorder__price")).filter(bookorder__price__gte=80).distinct()
    # for i in result:
    #     print(i)
    #     # Book object (1)
    #     # Book object (1)
    #     # Book object (1)
    #     # Book object (2)
    #     # Book object (2)
    # print(connection.queries)
    """'SELECT DISTINCT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, 
    `book`.`author_id`, `book`.`publisher_id`, `book_order`.`price` AS `order_price` FROM `book` 
    LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) INNER JOIN `book_order` 
    T3 ON (`book`.`id` = T3.`book_id`) WHERE T3.`price` >= 80.0e0'"""

    # 跟order_by使用的话也会将它当作一个字段
    result1 = Book.objects.filter(bookorder__price__gte=80).order_by('bookorder__price').distinct()
    for book in result1:
        print(book)
        # Book object (1)
        # Book object (1)
        # Book object (2)
        # Book object (2)
        # Book object (1)
    print(connection.queries)
    """'SELECT DISTINCT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, 
    `book`.`publisher_id`, `book_order`.`price` FROM `book` INNER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) 
    WHERE `book_order`.`price` >= 80.0e0 ORDER BY `book_order`.`price` ASC',"""
    return HttpResponse("index12")


def index13(request):
    # update更新
    # Book.objects.filter(id=4).update(price=F("price")+10)
    # print(connection.queries)
    # 'UPDATE `book` SET `price` = (`book`.`price` + 10) WHERE `book`.`id` = 4'

    # 全部书的价格上升10块
    # Book.objects.update(price=F("price")+10)
    # print(connection.queries)
    # {'sql': 'UPDATE `book` SET `price` = (`book`.`price` + 10)'

    # delete删除操作
    Author.objects.filter(id=6).delete()
    print(connection.queries)
    """
    {'sql': 'SELECT `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email` '
            'FROM `author` WHERE `author`.`id` = 6', 'time': '0.001'}, 
    {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, '
            '`book`.`publisher_id` FROM `book` WHERE `book`.`author_id` IN (6)', 'time': '0.001'}, 
    {'sql': 'DELETE FROM `author` WHERE `author`.`id` IN (6)', 'time': '0.003'}
    """
    return HttpResponse("index13")


def index14(request):
    # 切片操作
    books = Book.objects.all()[0:3]
    for book in books:
        print(book)
        # Book object (1)
        # Book object (2)
        # Book object (3)
    print(connection.queries)
    """
    {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, '
            '`book`.`author_id`, `book`.`publisher_id` FROM `book` LIMIT 3', 'time': '0.001'}
    """
    return HttpResponse("index14")