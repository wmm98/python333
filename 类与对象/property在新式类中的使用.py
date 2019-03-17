# 可读可写
class Person(object):
    def __int__(self):
        self.__age = 10

    @property
    def age(self):
        print("-----get----------")
        return self.__age

    @age.setter
    def age(self, value):
        print("--------set---------")
        self.__age = value


p = Person()
p.age = 30
print(p.age)

# --------set---------
# -----get----------
# 30




