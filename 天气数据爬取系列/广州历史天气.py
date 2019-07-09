#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


base_id = 'http://www.tianqihoubao.com/lishi/guangzhou/month/'


# In[20]:


weather_id = []
for year in range(2018, 2020):
    if year != 2019:
        for month in range(1, 13):
            base_id1 = ''
            if month < 10:
                m = '0' + str(month)
            else:
                m = str(month)
            base_id1 += base_id + str(year) + m + '.html'
            print(base_id1)
            weather_id.append(base_id1)
            
    else:
        for month1 in range(1,8):
            base_id1 = ''
            if month1 < 10:
                m1 = '0' + str(month1)
            else:
                m1 = str(month)
            base_id1 = base_id + str(year) + m1 + '.html'
            print(base_id1)
            weather_id.append(base_id1)


# In[21]:


weather_id


# In[23]:


len(weather_id)


# In[27]:


weather_data = []
for url in weather_id:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find('div',class_= 'wdetail')
    guanzhou = data.find_all('table')
    for table in guanzhou:
        for tr in table.find_all('tr')[1:]:
            td = tr('td')

            first = td[0].text.split()

            data = td[1].text.split()
            second = data[0] + data[1]
    #         print(second)

            first.append(second )

            data1 = td[2].text.split()
            third = data1[0] + data1[1] + data1[2]
            first.append(third )
    #         print(third)

            data2 = td[3].text.split()
            fourth = data2[0] + data2[1] + data2[2]
            first.append(fourth)

    #         print(first)
            weather_data.append(first)
        


# In[28]:


weather_data


# In[31]:


import pandas as pd
name_attribute = ['日期', '天气状况', '气温', '风力风向']
writerCSV=pd.DataFrame(columns=name_attribute, data=weather_data)
writerCSV.to_csv('D:\ 广州历史天气.csv')


# In[32]:


data = pd.read_csv('D:\ 广州历史天气.csv')


# In[37]:


data


# In[ ]:




