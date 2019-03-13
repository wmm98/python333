class A:
    @classmethod
    def leifangfa(cls, num):
        print('这是类方法', cls, num)


# 各种调用方法
A.leifangfa(66)

a = A
a.leifangfa(33)

result = A.leifangfa
result(55)

# 三种方法的调用结果
# 这是类方法 <class '__main__.A'> 66
# 这是类方法 <class '__main__.A'> 33
# 这是类方法 <class '__main__.A'> 55

class B(A):
    pass


b = B
b.leifangfa(99)  #这是类方法 <class '__main__.B'> 99
