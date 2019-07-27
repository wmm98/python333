from django.db import models
from datetime import datetime
from django.utils.timezone import now
from datetime import datetime


class Article(models.Model):
    # 如果想要使用自己定义的field来作为主键，，那么必须设置primary_key=True
    # bigint类型
    id = models.BigAutoField(primary_key=True)

    # 在定义字段的时候，如果没有指定null=True,那么默认情况下，null=False
    # 就是不能为空
    # 如果想要使用可以为null的BooleanField，那么应该使用NullBooleanField来代替
    # tinyint类型
    # # removed = models.BooleanField()
    removed = models.NullBooleanField()
    # # CharField 如果是超过254个字符， 那么就不建议使用
    # # 就推荐使用TextField, longtext
    # # varchar类型
    title = models.CharField(max_length=200)
    # auto_now_add:是在第一次添加数据进去的时候会自动获取当前时间，以后修改调用save()方法都不会更新时间
    create_time = models.DateTimeField(auto_now_add=True)

    # # DateField: 日期类型，在python中是date.date类型，在映射到数据据中也是date类型，使用这个fied可以传递一下几个参数
    # # 1.auto_now, 在每次数据保存得时候，都使用当前时间，比如作为一个记录修改日期的字段，可以将这个属性设置为True，即每次修改调用save方法都会更新时间
    # # 2.auto_now_add:在每次数据第一次被被添加的时候，都使用当前时间，比如作为第一个记录第一次入库的字段，可以将这个属性设置为True
    date = models.DateField(auto_now=True)

    # # DateTimeField:日期时间类型，类似于DateField，不仅可以存储日期，还可以存储时间，映射到数据库中是datetime类型，这个field也可以使用
    # # auto_now和auto_now_add两个属性
    date1 = models.DateTimeField(default=datetime.now)

    # # TimeField:时间类型，在数据库中是time类型，在python中是datetime.time类型
    time = models.TimeField(auto_now=True)

    def __str__(self):
        # <Article:(id, removed, title,date....)>
        return "<Article:({id}, {removed}, {title},{date},{date1},{time})>".format(id=self.id, removed=self.removed,
                                                                                   title=self.title,
                                                                                   date=self.date, date1=self.date1,
                                                                                   time=self.time)


class Person(models.Model):
    # EmailField 为字符串类型，没有传入参数默认最大长度为254
    # EmailField在数据库层面并不会限制字符串一定要满足邮箱格式
    # 只是以后在使用modelform等表单相关操作的时候会起作用
    email = models.EmailField()
    # 一样是字符串类型
    signature = models.TextField()


class Author(models.Model):
    username = models.CharField(max_length=100, null=True)  # 不写null=True就默认null=False
    age = models.IntegerField(null=True, db_column='author_age', default=0)  # db_column='author_age'修改字段名字
    create_time = models.DateTimeField(default=datetime.now)
    telephone = models.CharField(max_length=11, unique=True, null=True)

    # Meta配置
    class Meta:
        db_table = "author"  # 修改该表的名字
        # 然后就进行创建迁移文件，将迁移文件迁移到数据库
        ordering = ['age', 'username']  # 设置排序,时间相同就按照日期排序
        # ['-age']表示反序

# 创建迁移文件
# python manage.py makemigrations

# 将迁移文件迁移到数据库
# python manage.py migrate
