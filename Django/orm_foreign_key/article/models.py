from django.db import models


# ORM外键使用详解


# 父表
class Category(models.Model):
    name = models.CharField(max_length=100)


# def default_category():
#     return Category.objects.gte(pk=4)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField("Article")


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 表示外键参照Category表， on_delete:父表删除数据时影响字表，级别，CASCADE是可以删除，protect是不可以删除
    # on_delete = models.SET_NULL的时候删除父表的id，子表的id会被删除（前提是字表id可以为空），但是整条数据还在。
    # SET_DEFAULT时需要指定默认值，删除父表id的时候，补上默认的id,整行数据还在
    # category = models.ForeignKey("Category", on_delete=SET_DEFAULT, null=True, related_name='articles', default=Category.objects.get(pk=3)
    # SET()类似SET_DEFAULT
    # category = models.ForeignKey("Category", on_delete=models.SET(Category.objects.get(pk=4)), null=True, related_name='articles')

    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name='articles')
    #  在建好表的情况下再添加一个字段（外键）,null=True表示未添加之前的author为空
    author = models.ForeignKey("frontuser.FrontUser", on_delete=models.CASCADE, null=True)  # 引用另外一个app的模型

    # 调用时自动打印
    def __str__(self):
        return "<Article:(id:%s, title:%s)>" % (self.id, self.title)


#  引用自身作为外键,例如自己评论自己相关联
class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("self", on_delete=models.CASCADE)


