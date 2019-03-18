class Person:
    def __init__(self, a, n):
        self.age = a
        self.name = n

    # 面向用户
    def __str__(self):
        return "这个人的名字为年龄为 %d， 姓名为 %s" % (self.age, self.name)

    # 面向开发人员
    def __repr__(self):
        return "这个人的名字为年龄为 %d， 姓名为 %s" % (self.age, self.name)


p1 = Person(78, "张三")  # 这个人的名字为年龄为 78， 姓名为 张三
print(p1)
print(str(repr))  # <built-in function repr>

import datetime

t = datetime.datetime.now()
# 面向用户
print(t)  # 2019-03-18 16:47:03.343612
# 面向开发人员
print(repr(t))  # datetime.datetime(2019, 3, 18, 16, 46, 27, 264943)
print(eval(repr(t)))  # 2019-03-18 16:47:03.343612
