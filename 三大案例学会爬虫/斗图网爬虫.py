#  https://www.doutula.com/photo/list
# https://www.doutula.com/photo/list/?page=1

import requests
from bs4 import BeautifulSoup

BASE_URL_LIST = 'https://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []

for x in range(1, 870):
    url = BASE_URL_LIST + str(x)
    # print(url)
    PAGE_URL_LIST.append(url)

response = requests.get('https://www.doutula.com/photo/list/?page=1')
content = response.text

soup = BeautifulSoup(content, 'lxml')
soup.find_all('img', class_='img-responsive lazy image_dta loaded')

import urllib.request
url = 'http://img.doutula.com/production/uploads/image//2019/07/01/20190701957938_pJkKoN.jpg'
# req = urllib.request.Request(url)
urllib.request.urlretrieve(url, filename='test.jpg')