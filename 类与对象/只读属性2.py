# 前面学习了只读属性的实现，但在python中只有伪私有化，实际上通过底层的修改方法去重新赋值也是可以的
# class Person:
#
#     def __init__(self):
#         self.__age = 18  # 完全封闭
#
#     # 主要作用是可以以使用属性的方式来使用该方法
#     @property
#     def age(self):
#         return self.__age
#
#
# p = Person()
# # print(p.age)
# # # 18
#
# p.__dict__["_Person__age"] = 40
# print(p.age)  # 40成功修改__age的值


# 可以通过判定属性是否存在，如果存在的话，智能读取不能修改，不存在的话可以新增
class Person:

    def __setattr__(self, key, value):
        print(key, value)
        if key == "age" and key in self.__dict__.keys():
            print("只能读取该属性，不能修改")
        else:
            self.__dict__[key] = value


p = Person()
p.age = 18
print(p.age)

# p.age = 10
# print(p.age)
# 只能读取该属性，不能修改
# 18
# print(p.__dict__)  {'age': 18}

p.name = "李四"
print(p.name)
print(p.__dict__)

# name 李四
# 李四
# {'age': 18, 'name': '李四'}

p.name = "张三"
print(p.__dict__)

