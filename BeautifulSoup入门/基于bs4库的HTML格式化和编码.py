import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

print(soup.a.prettify())
# <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
# Basic Python
# </a>
print(soup.prettify())