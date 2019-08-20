import pandas as pd
import pymysql
import numpy as np

# 加上字符集参数，防止中文乱码
dbconn = pymysql.connect(
    host="localhost",
    database="weather",
    user="root",
    password="123456",
    port=3306,
    charset='utf8'
)

# sql语句
sqlcmd = "select id,date1,Weather_condition1, Weather_condition2, high_temperature, " \
         "low_temperature, Wind_direction1, Wind_direction2 from foshan_weather"

# 利用pandas 模块导入mysql数据
a = pd.read_sql(sqlcmd, dbconn)
# print(a)
# 取前5行数据
# b = a.head()
# print(b)

a_list = np.array(a)
# print(a_list)

for i in a_list:
    print(i)
