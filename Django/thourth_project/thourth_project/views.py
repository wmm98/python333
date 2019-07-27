from django.shortcuts import render


# def index(request):
#     return render(request, 'index.html')

# 模板变量详解
# 通过参数传到html上
# def index(request):
#     context = {
#         'username': 'Django'
#     }
#     return render(request, 'index.html', context=context)

class Person:
    def __init__(self, user_name):
        self.user_name = user_name


# 1>当p时是一个对象的时候
# def index(request):
#     user_name = Person("Django11")
#     context = {
#         'person': user_name
#     }
#
#     # 2>当p是一个字典的时候
#
#     return render(request, '类.html', context=context)

# 2>当p是一个字典的时候
# def index(request):
#     context = {
#         'person': {
#             'user_name': 'python11',
#             'user_name1': 'python22'
#         }
#     }
#
#     # 2>当p是一个字典的时候
#
#     return render(request, '字典.html', context=context)

def index(request):
    context = {
        'person': [
            'python11',
            'python22'
        ]
    }

    # 2>当p是一个列表的时候

    return render(request, '列表.html', context=context)

#  模板中的变量同样也支持（.）的形式，在出现了点的情况，比如person.username,模板是按照一下模式进行解释的:
# 1> 如果person是一个字典，那么就会查找字典的uername这个key对应的值
# 2> 如果person是一个对象，那么就会查找这个对象的username属性，或者是username这个方法
# 3> 如果出现的是person.1，会判断person是否一个列表或者元组或者任意的可以通过下标访问的对象，如果是的话就取这个列表的第一个值，
# 如果不是就会获取一个空的字符串

# 注意：不能通过中括号访问字典或列表中的值，比如dict[key]和list[1]是不支持的
