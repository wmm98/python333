import requests
from bs4 import BeautifulSoup
import bs4

#  步骤一：从网络上获取大学排名网页内容
#  步骤二： 提取网页内容中信息到合适的数据结构
#  步骤三： 利用数据结构展示并输出结果

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

def main():
    unifo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)  # 打印前20个大学

main()
