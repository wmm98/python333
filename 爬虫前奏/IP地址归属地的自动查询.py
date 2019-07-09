import requests

url = "http://m.ip138.com/ip.asp?ip="  #查ip的网址
ip = '202.204.80.112'  # 需要查询的地址
try:
    r = requests.get(url + ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")