import requests


# 测试部分
# r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y')
# print(r.status_code)
# print(r.encoding)
# # 访问失败
# # 503
# # ISO-8859-1
#
# # 直接访问会报错
# # print(r.text)
#
# r.encoding = r.apparent_encoding
# # 查看错误信息
# print(r.text)
# # <font color="red">抱歉，由于程序执行时，遇到意外错误，您刚刚操作没有执行成功，请稍后重试。或将此错误报告给我们的客服中
#
# print(r.request.headers)
# # {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#
# kv = {'user-agent': 'Mozilla/5.0'}
# r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y', headers=kv)
# print(r.request.headers)
# # {'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
#
# print(r.text)
# #  当访问失败的时候，可以改变头部的user-agent

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()  # 如果状态码不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return r.text[1000:2000]
    except:
        return "爬取失败"


url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
print(getHTMLText(url))
