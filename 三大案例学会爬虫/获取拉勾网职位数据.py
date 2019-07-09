import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': 'privacyPolicyPopup=false; user_trace_token=20190605141645-0c5bcd49-c907-4e76-a92f-e3f3943ff4d2; _ga=GA1.2.1716859418.1559715407; LGUID=20190605141646-7f197271-8759-11e9-aa13-525400f775ce; LG_HAS_LOGIN=1; index_location_city=%E5%B9%BF%E5%B7%9E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559715481,1559715515,1559715589,1562210932; JSESSIONID=ABAAABAAAGFABEF94B4DC70617B1768D8A9F0F4D4351C04; _gid=GA1.2.479204572.1562211049; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; LGSID=20190704155345-d98ed0f4-9e30-11e9-a4d9-5254005c3644; privacyPolicyPopup=false; LG_LOGIN_USER_ID=85b5cc2685719f2c0fa132e4c0cfdf8fb9fc18118ebc61007fef93434f6aed1c; _putrc=F3563EE66783A21B123F89F2B170EADC; login=true; unick=%E5%90%B4%E5%B0%8F%E5%A7%90; gate_login_token=36f66f35ddf41132d307c250e437bc464e858e33234a39ae13a515dc7e376c9a; TG-TRACK-CODE=search_code; _gat=1; X_HTTP_TOKEN=b0414f33081428bb0410322651ae8d2b63b68617fa; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562230141; LGRID=20190704164900-917730f2-9e38-11e9-a4d9-5254005c3644; SEARCH_ID=49aa5685b7e945d0a0487f777aaaa2cf',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': None,
    'X-Requested-With': 'XMLHttpRequest'

}

# 属于post数据
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'java'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false', headers=headers, data=data)
# print(r.status_code)
# print(r.text)

print(response.json())
print("----------------------------------------------------------------")

positions = response.json()['content']['positionResult']['result']

print(positions)
print("----------------------------------------------------------------")

for po in positions:
    for p, k in po.items():
        print(p, ':', k)
    print()

