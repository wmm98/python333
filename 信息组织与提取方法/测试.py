import scrapy
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.burdastyle.com/pattern_store/patterns?page=1')
soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.prettify())

# def parse(self, response):
#     bs = BeautifulSoup(response.body, 'lxml')     #创建BS对象
#     patt_obj = bs.find('ul', class_='patterns-list')
#     det_tag_list = patt_obj.find_all('li')
#     for det_tag in det_tag_list:
#         pi = PatterItem()
#         if det_tag.find('a') is not None:
#             pi['patt_id'] = det_tag.find('a').text
#         if det_tag.find('li', class_='price') is not None:
#             pi['patt_price'] = det_tag.find('li', class_='price').text
#     yield pi

patt_obj = soup.find('ul', class_='patterns-list')


price_list = []
name_list = []
for li in patt_obj.find_all('li'):
    for h in li.find_all('h3'):
        name_list.append(h.text)
    for price in li.find_all('li', class_="price"):
    #     print(price.text.split())
        price_list.append(price.text.split())
# print(len(name_list))
# print(len(price_list))

# for i in name_list:
#     print(i)

print(price_list)

print("------------------------")
p_list = []
for j in price_list:
    for j1 in j:
        p_list.append(j1)
print(p_list)

t_list = []
for name_price in range(len(name_list)):
    t_list.append([name_list[name_price], p_list[name_price]])
print(t_list)

# import pandas as pd
# name_attribute = ['name', 'price']
# writerCSV=pd.DataFrame(columns=name_attribute, data=t_list)
# writerCSV.to_csv('D:\ foods.csv', encoding='utf-8')

