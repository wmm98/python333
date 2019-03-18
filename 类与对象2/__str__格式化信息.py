class Person:
    def __init__(self, a, n):
        self.age = a
        self.name = n

    def __str__(self):
        return "这个人的名字为年龄为 %d， 姓名为 %s" % (self.age, self.name)


p1 = Person(78, "张三")
print(p1)

p2 = Person(12, "李四")
print(p2)

s = str(p1)
print(s)
s1 = str(p2)
print(s1)

# 这个人的名字为年龄为 78， 姓名为 张三
# 这个人的名字为年龄为 12， 姓名为 李四
# 这个人的名字为年龄为 78， 姓名为 张三
# 这个人的名字为年龄为 12， 姓名为 李四
