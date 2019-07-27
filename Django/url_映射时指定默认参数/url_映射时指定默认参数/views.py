from django.http import HttpResponse

book_list = [
    '三国演义',
    '水浒传',
    '红楼梦',
    '西游记'
]


def books(request, page=0):
    return HttpResponse(book_list[page])

# 默认page=0，当不传参数的时候跳到第0个，相当于第一页
