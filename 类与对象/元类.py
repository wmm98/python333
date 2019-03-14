class A:
    pass


a = A()
print(a.__class__)  # <class '__main__.A'>  实例化对象是由类创建出来的
print(A.__class__)  # <class 'type'>类是由type即元类创建出来的

num = 10
print(num.__class__)  # <class 'int'> 10是由int 类创建出来的
print(int.__class__)  # <class 'type'>int类也是由元类创建出来 的

l = "oooo"
print(l.__class__)  # <class 'str'>
print(str.__class__)  #<class 'type'>

