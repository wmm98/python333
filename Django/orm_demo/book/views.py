from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


def index(request):
    # 1.使用ORM添加一条数据到数据库中
    # book = Book(name='偷影子的人', author='马克李维', price=300)
    # book.save()
    # book = Book(name='且听风吟', author='村上春树', price=200)
    # book.save()

    # 2.查询
    # 2.1 根据主键进行查找
    # primary key
    # book = Book.objects.get(pk=2)
    # print(book)
    # <Book:(且听风吟, 村上春树, 200.0)>

    # 2.2根据其他条件进行查找
    # books = Book.objects.filter(name='偷影子的人')
    # print(books)
    # <QuerySet [<Book: <Book:(偷影子的人, 马克李维, 300.0)>>]>
    # print(books.first())
    # <Book:(偷影子的人, 马克李维, 300.0)>

    # 3.删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()

    # 4.修改数据
    book = Book.objects.get(pk=2)
    book.price = 190
    book.save()
    return HttpResponse("图书添加成功！")


