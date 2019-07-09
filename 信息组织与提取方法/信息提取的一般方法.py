import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
# print(demo)

soup = BeautifulSoup(demo, "html.parser")

#  提取html中所有的url
for link in soup.find_all('a'):
    print(link.get('href'))

# http://www.icourse163.org/course/BIT-268001
# http://www.icourse163.org/course/BIT-1001870001