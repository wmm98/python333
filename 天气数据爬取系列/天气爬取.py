import requests
from bs4 import BeautifulSoup
import mysql.connector
import numpy as np

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="weather"  # 先自己手动创建数据库
)

mycursor = mydb.cursor()

# 数据表只能创建一次
# mycursor.execute("CREATE TABLE kugou (id INT AUTO_INCREMENT PRIMARY KEY, rank VARCHAR(255), singer VARCHAR(255), song VARCHAR(255), time VARCHAR(255))")
# mycursor.execute("CREATE TABLE huizhou_weather (id INT AUTO_INCREMENT PRIMARY KEY, date1 VARCHAR(20), "
#                  "Weather_condition1 VARCHAR(10),Weather_condition2 VARCHAR(10), high_temperature VARCHAR(10), "
#                  "low_temperature VARCHAR(10), Wind_direction1 VARCHAR(50),Wind_direction2 VARCHAR(50))")

sql = "INSERT INTO huizhou_weather (date1, Weather_condition1, Weather_condition2, high_temperature, low_temperature, Wind_direction1, Wind_direction2) VALUES (%s, %s, %s, %s, %s, %s, %s)"

base_id = 'http://www.tianqihoubao.com/lishi/huizhou/month/'

weather_id = []
for year in range(2015, 2020):
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
        for month1 in range(1, 9):
            base_id1 = ''
            if month1 < 10:
                m1 = '0' + str(month1)
            else:
                m1 = str(month)
            base_id1 = base_id + str(year) + m1 + '.html'
            print(base_id1)
            weather_id.append(base_id1)

weather_data = []
for url in weather_id:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find('div', class_='wdetail')
    guanzhou = data.find_all('table')
    for table in guanzhou:
        for tr in table.find_all('tr')[1:]:
            td = tr('td')

            first = td[0].text.split()

            data = td[1].text.split()
            # print(data)
            second = data[0] + data[1]
            #         print(second)

            first.append(second)

            data1 = td[2].text.split()
            # print(url)
            if len(data1) == 2:
                third = data1[0] + data1[1]
            elif len(data1) == 1:
                third = data1[0]
            else:
                third = data1[0] + data1[1] + data1[2]
            first.append(third)
            #         print(third)

            data2 = td[3].text.split()
            # print(data2)
            if len(data2) == 1:
                fourth = data2[0]
            elif len(data2) == 2:
                fourth = data2[0] + data2[1]
            else:
                fourth = data2[0] + data2[1] + data2[2]
            first.append(fourth)

            #         print(first)
            weather_data.append(first)
# for i in weather_data:
#     print(i)


# new_weather = []
for i in weather_data:
    data3 = i[1].split('/')
    data4 = i[2].split('/')
    data5 = i[3].split('/')
    weather = (i[0], data3[0], data3[1], data4[0], data4[1], data5[0], data5[1])
    mycursor.execute(sql, weather)
    mydb.commit()

    # new_weather.append(weather)
