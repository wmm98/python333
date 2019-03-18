class Person:
    def __call__(self, *args, **kwargs):  # **表示以字典的形式接收参数
        print(args, kwargs)


# 这时候实例化出来的对象具有调用能力
p = Person()
p(1, 2, name="hqn")
# (1, 2) {'name': 'hqn'}
