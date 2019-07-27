from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)

    # 打印
    def __str__(self):
        # <Book:(name, author, price)>
        return "<Book:({name}, {author}, {price})>".format(name=self.name, author=self.author, price=self.price)

# 创建迁移文件
# python manage.py makemigrations

# 将迁移文件迁移到数据库
# python manage.py migrate
