import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.weather.com.cn/textFC/hn.shtml#1')
r.encoding = r.apparent_encoding
print(r.text)