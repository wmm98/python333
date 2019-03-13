class A:
    @staticmethod
    def jingtaifangfa():
        print('这是静态方法')


# 各种调用方法
A.jingtaifangfa()

a = A
a.jingtaifangfa()

result = A.jingtaifangfa
result()

# 这是静态方法
# 这是静态方法
# 这是静态方法
