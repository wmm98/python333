from django.http import HttpResponse, JsonResponse
import json


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


def jsonresponse_view(request):
    # Jsonresponse类：用来对象dump成json字符串，然后返回将json字符串封装成Response对象返回给浏览器
    # 并用他的content-type是application/json

    person = {
        'username': 'zhiliao',
        'age': 18,
        'height': 180
    }

    # person_str = json.dumps(person)
    # response = HttpResponse(person_str, content_type='application/json')
    # # {"username": "zhiliao", "age": 18, "height": 180}
    # return response

    # 等同于以上用法
    return JsonResponse(person)
    # {"username": "zhiliao", "age": 18, "height": 180}


# 默认情况下JsonResponse只能对字典进行dump,如果非要对非字典的数据进行dump,那么需要给JsonResponse传递一个safe=False的参数
def index1(request):
    person = ['zhiliao', 18, 180]
    return JsonResponse(person, safe=False)
    # ["zhiliao", 18, 180]
