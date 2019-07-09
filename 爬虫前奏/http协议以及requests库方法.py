import requests

r = requests.head("https://www.icourse163.org/learn/BIT-1001870001?tid=1206093223#"
                 "/learn/content?type=detail&id=1210598247&cid=1212806705&replay=true")

print(r.headers)

print("------------------------------------------------------------------")

r = requests.post("http://httpbin.org/post")
print(r.text)

print("------------------------------------------------------------------")

r = requests.post("http://httpbin.org/post", data='ABC')
print(r.text)

print("------------------------------------------------------------------")

payload = {'key': 'value1', 'key2': 'vaule2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

print("------------------------------------------------------------------")

payload = {'key1': 'value1', 'key2': 'vaule2'}
r = requests.post("http://httpbin.org/put", data=payload)
print(r.text)