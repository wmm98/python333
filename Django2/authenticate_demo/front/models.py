from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# get_user_model可以直接获取到在settings配置的model,比较安全
from django.contrib.auth import get_user_model

# 如果模型是一个代理模型，那么就不能在这个模型中添加新的字段


"""
1. 设置Proxy模型：
如果你对Django提供的字段，以及验证的方法都比较满意，没有什么需要改的。
但是只是需要在他原有的基础之上增加一些操作的方法。
那么建议使用这种方式。示例代码如下：
"""
# class Person(User):
#     class Meta:
#         proxy = True
#
#     # 类方法
#     @classmethod
#     def get_blacklist(cls):
#         # 获取黑名单
#         return cls.objects.filter(is_active=False)


"""
在以上，我们定义了一个Person类，让他继承自User，并且在Meta中设置proxy=True，说明这个只是User的一个代理模型。
他并不会影响原来User模型在数据库中表的结构。以后如果你想方便的获取所有黑名单的人，那么你就可以通过
Person.get_blacklist()就可以获取到。并且User.objects.all()和Person.objects.all()其实是等价的。
因为他们都是从User这个模型中获取所有的数据
"""

"""
2. 一对一外键：
如果你对用户验证方法authenticate没有其他要求，就是使用username和password即可完成。
但是想要在原来模型的基础之上添加新的字段，那么可以使用一对一外键的方式。示例代码如下：
"""

# class UserExtension(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)


"""
以上定义一个UserExtension的模型，并且让她和User模型进行一对一的绑定，以后我们新增的字段，就添加到UserExtension上。
并且还写了一个接受保存模型的信号处理方法，只要是User调用了save方法，那么就会创建一个UserExtension和User进行绑定
"""

# @receiver(post_save, sender=User)
# def handler_user_extension(sender, instance, created, **kwargs):
#     # instance 表示当前对象
#
#     # 第一次创建数据的时候，进行user和UserExtension进行绑定
#     if created:
#         UserExtension.objects.create(user=instance)
#     else:
#         # 否则修改属性
#         instance.extension.save()


"""
3.对于authenticate不满意，并且不想要修改原来User对象上的一些字段，但是想要增加一些字段，
那么这时候可以直接继承自django.contrib.auth.models.AbstractUser，其实这个类也是django.contrib.auth.models.User的父类。
比如我们想要在原来User模型的基础之上添加一个telephone和school字段。
"""


# 重写objects方法，因为objects还会调用原来user里的username验证
# objects类型就是BaseUserManager模型，需要重新定义
class UserManager(BaseUserManager):
    # 受保护函数，只能在该类中调用
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('必须要传递手机号码')
        if not password:
            raise ValueError("必须要传递密码")
        # self.model指User
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    # 创建普通用户
    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)

    # 创建超级用户
    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)


# 不直接继承user的原因是user是直接继承AbstractUser,而且user并没有在原来的基础上添加任何字段
# class User(AbstractUser):
#     telephone = models.CharField(max_length=11, unique=True)
#     school = models.CharField(max_length=100)
#
#     USERNAME_FIELD = 'telephone'
#
#     objects = UserManager()

# 扩展完模型之后需要在setting中设置，说明不是用django内置的模型
# 然后再在settings中配置好AUTH_USER_MODEL=youapp.User。
# 这种方式因为破坏了原来User模型的表结构，所以必须要在第一次migrate前就先定义好。

"""
4. 继承自AbstractBaseUser模型：
如果你想修改默认的验证方式，并且对于原来User模型上的一些字段不想要，那么可以自定义一个模型，然后继承自AbstractBaseUser，
再添加你想要的字段。这种方式会比较麻烦，最好是确定自己对Django比较了解才推荐使用。步骤如下：

创建模型。示例代码如下：
"""


class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'telephone'
    # 命令行创建的时候需要填的字段
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_sort_name(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)