# class Animal:
#     __x = 10  # 两个_表示私有属性,模块内（本类）的除了本模块内，其他地方都访问不了
#
#     def test(self):
#         print(Animal.__x)
#         print(self.__x)
#         pass
#
#
# class Dog(Animal):
#     def test2(self):
#         print(Dog.__x)
#         print(self.__x)
#         pass
#

# 测试带代码
# a = Animal()
# a.test()
# 10
# 10

# d = Dog()
# d.test2()
# AttributeError: type object 'Dog' has no attribute '_Dog__x'
#  报错，不能访问父类的受保护属性

__all__ = ["__a"]  # 这样之后跨领域就可以访问了
__a = 20  # 这种情况下，跟私有属性的的情况一样
