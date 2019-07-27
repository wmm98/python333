from django.db import models


class FrontUser(models.Model):
    username = models.CharField(max_length=200)

    # 直接调用
    def __str__(self):
        return "<FrontUser:(id:%s, username:%s)>" % (self.id, self.username)


# 直接打印
# def __str__(self):
#     # <Article:(id, removed, title,date....)>
#     return "<Article:({id}, {removed}, {title},{date},{date1},{time})>".format(id=self.id, removed=self.removed,
#                                                                                title=self.title,


# 一对一,就是说外键是唯一的
# 这里的参数最好使用CASCADE，因为要删除用户时，用户信息也要删除
class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser", on_delete=models.CASCADE)

    def __str__(self):
        return "<UserExtension:(id:%s,school:%s, user_id:%s)>" % (self.id, self.school, self.user_id)
