import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

url = "http://www.baidu.com"
print(getHTMLText(url))