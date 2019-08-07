from django.http import HttpResponse


def index(request):
    # 返回content为知了课堂
    # response = HttpResponse('<h1>知了课堂</h1>')

    # content_type='text/plain，将content解析为纯文本
    response = HttpResponse('<h1>知了课堂</h1>', content_type='text/plain; charset=utf-8')
    # Content-Type: text/plain; charset=utf-8

    # 设置状态码
    response.status_code = 400
    # Status Code: 400 Bad Request

    # 设置请求头，例如
    response['X-Token'] = 'zhiliao'
    # X-Token: zhiliao

    # write：HttpResponse是一个类似于文件的对象，可以用来写入数据到数据体中
    response.write("wmmmm")
    # <h1>知了课堂</h1>wmmmm
    return response
