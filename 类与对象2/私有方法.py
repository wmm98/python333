class Person:
    __age = 34

    def __run(self):
        print("跑步的鱼-------------")


p = Person()
# p.__run()   # AttributeError: 'Person' object has no attribute '__run'

print(Person.__dict__)
#  {'__module__': '__main__', '_Person__age': 34, '_Person__run': <function Person.__run at 0x000001EA242552F0>
p._Person__run()
# 跑步的鱼-------------
