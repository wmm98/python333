import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
# print(demo)

soup = BeautifulSoup(demo, "html.parser")
print(soup)
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)

print(len(soup.body.contents))
print(soup.body.contents[1])
print("----------------------------------------------------------")


#  遍历儿子节点
for child in soup.body.children:
    print(child)

print("*******************************************")

#  遍历子孙节点
for child1 in soup.body.children:
    print(child1)

#  还可已用contents表示,返回列表类型
for i in soup.body.contents:
    print(i)

print("*******************************************")

#  标签树的上行遍历
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# 遍历结果
# p
# body
# html
# [document]

print("*******************************************")


#  平行遍历
# 平行遍历发生在同一个父节点下的各节点间
# 1>遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)

print("*******************************************")
# 2>遍历前续节点
for sibling1 in soup.a.previous_siblings:
    print(sibling1)