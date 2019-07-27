class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("这是父类A")

class B(A):
    def __init__(self):
        print("这是子类B")
    def run(self):
        print("-------在跑")

class C(B):
    def __init__(self):
        # super().__init__()
        # print("这是C")

    def run1(self):
        print("%%%%%%%%%%%%%%5")
        print(self.name, self.age)
        super().run()


c = C("小红", 23)
print(c.run1())