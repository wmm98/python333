class Person:

    # 主要作用是当我们创建好一个实例对象之后，会自动调用这个方法，来初始化这个对象
    def __init__(self):
        self.__age = 18  # 默认

    # 设置一个方法来赋值给age
    def setAge(self, value):
        if isinstance(value, int) and 0 < value < 100:
            self.__age = value
        else:
            print("请正确输入")

    # 由于在模块外部我们一般是不会直接访问是由属性的，这种情况下就会采用方法来返回私有属性的值
    def getAge(self):
        return self.__age


p = Person()
p.setAge(20)
print(p.getAge())
