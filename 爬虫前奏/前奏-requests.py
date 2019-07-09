import requests

r = requests.get("https://www.icourse163.org/learn/BIT-1001870001?tid=1206093223#"
                 "/learn/content?type=detail&id=1210598247&cid=1212806705&replay=true")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
# r.encoding = 'utf-8'
print(r.text)