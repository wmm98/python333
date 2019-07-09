import requests

# 测试为看可爬取
# r = requests.get('https://item.jd.com/100000822981.html')
# print(r.status_code)
# print(r.encoding)
# print(r.apparent_encoding)

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


url = "https://item.jd.com/100000822981.html"
print(getHTMLText(url))