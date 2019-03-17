class Person:
    """"
    关于这个类的描述，类的作用，类的构造函数等等；类属性的描述
    Attributes:
        count: int 代表是人的个数
    """

    # 代表是人的个数
    count = 10

    def run(self, distance, step):

        print("人在跑")
        return distance / step