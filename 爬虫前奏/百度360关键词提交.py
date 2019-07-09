import requests


def getHTMLText(url):
    try:
        kv = {'wd': 'python'}
        r = requests.get(url, params=kv)
        r.raise_for_status()  # 如果状态码不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return len(r.text)
    except:
        return "爬取失败"


url = 'http://www.baidu.com/s'
print(getHTMLText(url))
