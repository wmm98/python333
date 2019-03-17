class Person:

    def __init__(self):
        self.__age = 18  # 完全封闭

    # 主要作用是可以以使用属性的方式来使用该方法
    @property
    def age(self):
        return self.__age


p = Person()
print(p.age)
# 18

# 这种情况下出错，因为只读不能写
# p.age= 9
# print(p.age)
# AttributeError: can't set attribute



