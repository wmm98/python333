
#  动态创建类，用type创建
def run(self):
    print(self, "000000000000000000000000")


dog = type("Dog", (), {"毛": "黑色", "年龄": 2, "run": run})
print(dog.__dict__)
# {'毛': '黑色', '年龄': 2, 'run': <function run at 0x000001C3379B6488>, '__module__': '__main__',
#  '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakre
print(dog)  # <class '__main__.Dog'>  就是一个类，名Dog

# 创建一个对象
dog1 = dog()
# 调用实例方法
dog1.run()  # <__main__.Dog object at 0x0000024A8C5A9780> 000000000000000000000000

