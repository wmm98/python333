from django.http import HttpResponse, JsonResponse
from .models import *
from django.views import View
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from django.forms.models import model_to_dict
import datetime
import requests
from bs4 import BeautifulSoup
import os
import random
import pandas as pd
import xlrd


# 生成csv文件
def get_data1(m_model):
    weather_data = m_model.objects.values_list()
    # print(list(data))
    # print(weather_data[:5])

    name_attribute = ['序号', '日期', '天气状况1', '天气状况2', '最高温', '最低温', '风力风向1', '风力风向2']
    writerCSV = pd.DataFrame(columns=name_attribute, data=weather_data)
    writerCSV.to_csv('D:\课\Django\天气数据\数据.csv')


# 预处理之后的数据
def deal_data():
    # 调用函数生成csv文件
    # get_data1()
    # 打开数据文件
    data = pd.read_csv('D:\课\Django\天气数据\数据.csv')
    data = data.drop(['日期'], axis=1)
    data = data.drop(['Unnamed: 0'], axis=1)
    data = data.drop(['序号'], axis=1)
    # print(data.head())

    # 处理天气状况1
    one_dic = {}
    i = -1
    for i1 in data['天气状况1']:
        if i1 in one_dic:
            pass
        else:
            i += 1
            one_dic[i1] = one_dic.get(i1, i)
    data['Weather_condition1'] = data['天气状况1'].map(one_dic)
    # print(data.head())

    # 天气状况2
    two_dic = {}
    j = -1
    for j1 in data['天气状况2']:
        if j1 in two_dic:
            pass
        else:
            j += 1
            two_dic[j1] = two_dic.get(j1, j)
    data['Weather_condition2'] = data['天气状况2'].map(two_dic)
    # print(data.head())

    # 最高温
    high_weather = {}
    k = -1
    for k1 in data['最高温']:
        if k1 in high_weather:
            pass
        else:
            k += 1
            high_weather[k1] = high_weather.get(k1, k)
    data['high_temperature'] = data['最高温'].map(high_weather)
    # print(data.head())

    # 最低温
    low_weather = {}
    m = -1
    for m1 in data['最低温']:
        if m1 in low_weather:
            pass
        else:
            m += 1
            low_weather[m1] = low_weather.get(m1, m)
    data['low_temperature'] = data['最低温'].map(low_weather)
    # print(data.head())

    # 风力风向1
    wind1 = {}
    n = -1
    for n1 in data['风力风向1']:
        if n1 in wind1:
            pass
        else:
            n += 1
            wind1[n1] = wind1.get(n1, n)
    data['Wind_direction1'] = data['风力风向1'].map(wind1)

    # 风力风向2
    wind2 = {}
    x = -1
    for x1 in data['风力风向2']:
        if x1 in wind2:
            pass
        else:
            x += 1
            wind2[x1] = wind2.get(x1, x)
    data['Wind_direction2'] = data['风力风向2'].map(wind2)

    # 标签
    # 最高温标签
    high_temperature_label = np.array(data['high_temperature'])
    # 最低温
    low_temperature_label = np.array(data['low_temperature'])
    # 天气状况1
    Weather_condition1_label = np.array(data['Weather_condition1'])
    # 天气状况2：
    Weather_condition2_label = np.array(data['Weather_condition2'])
    # 风力风向1
    Wind_direction1_label = np.array(data['Wind_direction1'])
    # 风力风向2
    Wind_direction2_label = np.array(data['Weather_condition2'])

    # name_attribute = ['序号', '日期', '天气状况1', '天气状况2', '最高温', '最低温', '风力风向1', '风力风向2']
    data = data.drop(['天气状况1'], axis=1)
    data = data.drop(['天气状况2'], axis=1)
    data = data.drop(['最高温'], axis=1)
    data = data.drop(['最低温'], axis=1)
    data = data.drop(['风力风向1'], axis=1)
    data = data.drop(['风力风向2'], axis=1)
    # 返回的带有列名称的数据集
    data_set = data
    # print(data.head())

    # 纯数字数据集
    # dataSet = np.array(data)[:, 6:]

    # 测试数据,取最后一条数据
    # test_data = dataSet[-1:, :]

    # 返回一个列表，有各类标签和数据集,
    list_data = [high_temperature_label, low_temperature_label, Weather_condition1_label, Weather_condition2_label,
                 Wind_direction1_label, Wind_direction2_label, one_dic, two_dic, high_weather, low_weather, wind1,
                 wind2, data_set]
    return list_data


# 决策树算法
def tree_predict(x_train, x_test, y_train):
    # print("这是tree_predict方法")
    tree_model = tree.DecisionTreeClassifier().fit(x_train, x_test)
    # print("这是tree_predict方法")
    predict_result = tree_model.predict(y_train)
    # print("这是tree_predict方法")
    return predict_result


# 返回今天的数据
def today_condiction(city):
    url = 'http://www.tianqihoubao.com/yubao/%s.html' % city
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find('div', class_='wdetail')
    guanzhou = data.find_all('table')
    weather_data = []
    for table in guanzhou:
        for tr in table.find_all('tr')[1:]:
            td_list = []
            for td in tr.text.split():
                td_list.append(td)
            #                 print(td)
            #             print(td_list)
            weather_data.append(td_list)

    day = []
    night = []
    for i in range(0, len(weather_data)):
        if i % 2 == 0:
            day.append(weather_data[i])
        else:
            night.append(weather_data[i])

    today_white = day[1]
    today_night = night[1][1:]

    today_weather = [today_white[0], today_white[3][:-1], today_night[1][:-1], today_white[2], today_night[0],
                     today_white[4] + today_white[5],
                     today_night[2] + today_night[3]]
    print(today_weather)
    return today_weather


# 各个字段的测试数据
def every_col_test():
    # 预测明天的数据
    # col_names = ['high_temperature', 'low_temperature', 'weather_condition1', 'weather_condition2', 'wind_direction1','wind_direction2']
    high_temperature_test = TestData1.objects.all().values('low_temperature', 'weather_condition1',
                                                           'weather_condition2', 'wind_direction1', 'wind_direction2')
    high_temperature_test = list(list(high_temperature_test)[-1].values())
    # print("=======转化=========")
    # print(high_temperature_test)

    low_temperature_test = TestData1.objects.all().values('high_temperature', 'weather_condition1',
                                                          'weather_condition2', 'wind_direction1', 'wind_direction2')
    low_temperature_test = list(list(low_temperature_test)[-1].values())
    # print(low_temperature_test)
    # print("================")

    weather_condition1_test = TestData1.objects.all().values('high_temperature', 'low_temperature',
                                                             'weather_condition2', 'wind_direction1', 'wind_direction2')
    weather_condition1_test = list(list(weather_condition1_test)[-1].values())
    # print(weather_condition1_test)

    weather_condition2_test = TestData1.objects.all().values('high_temperature', 'low_temperature',
                                                             'weather_condition1', 'wind_direction1', 'wind_direction2')
    weather_condition2_test = list(list(weather_condition2_test)[-1].values())
    # print(weather_condition2_test)

    wind_direction1_test = TestData1.objects.all().values('high_temperature', 'low_temperature', 'weather_condition1',
                                                          'weather_condition2', 'wind_direction2')
    wind_direction1_test = list(list(wind_direction1_test)[-1].values())
    # print(wind_direction1_test)

    wind_direction2_test = TestData1.objects.all().values('high_temperature', 'low_temperature', 'weather_condition1',
                                                          'weather_condition2', 'wind_direction1')
    wind_direction2_test = list(list(wind_direction2_test)[-1].values())
    # print(wind_direction2_test)

    result = [[np.array(high_temperature_test)], [np.array(low_temperature_test)], [np.array(weather_condition1_test)],
              [np.array(weather_condition2_test)],
              [np.array(wind_direction1_test)], [np.array(wind_direction2_test)]]
    # print("**********明天测试数据**************")
    # print(type(result[0]))
    # print(result[0])
    # print("*******************************")
    # print(len(result))
    return result


# 预测数据
def data_predict():
    # 一周的时间
    today = datetime.date.today()
    date_days = [str(today)]
    for d in range(1, 7):
        futrue_day = today + datetime.timedelta(days=d)
        date_days.append(str(futrue_day))

    # 调用处理好的数据
    list_data = deal_data()
    # 标签
    # high_temperature_label = list_data[0]
    # low_temperature_label = list_data[1]
    # Weather_condition1_label = list_data[2]
    # Weather_condition2_label = list_data[3]
    # Wind_direction1_label = list_data[4]
    # Wind_direction2_label = list_data[5]

    # 返回字典数据
    # dict_data = {}

    # 各标签对应的数字
    # Weather_condition1_dict = list_data[6]
    # Weather_condition2_dict = list_data[7]
    # high_weather_dict = list_data[8]
    # low_weather_dict = list_data[9]
    # Wind_direction1_dict = list_data[10]
    # Wind_direction2_dict = list_data[11]

    # 数据集
    data_set = list_data[12]
    # 测试数据
    # test_data = list_data[13]

    # 复制数据集来预测数据
    dataSet = data_set.copy()
    # 预测最高温，drop掉最高温列
    high_temperature_predict_data = dataSet.drop(['high_temperature'], axis=1)
    # 训练数据集
    high_temperature_train = np.array(high_temperature_predict_data)
    high_temperature_label = list_data[0]
    # 测试数据
    high_temperature_test = np.array(high_temperature_predict_data)[-1:]
    high_weather_dict = list(list_data[8].items())

    # dict_data["high_temperature_data"] = [high_temperature_train, high_temperature_test]
    # dict_data["high_temperature_labels"] = high_temperature_label
    # dict_data["high_temperature_dict"] = high_weather_dict
    # print("======================================================")
    # print(dict_data)
    # print("======================================================")

    # 划分预测最低温数据
    dataSet1 = data_set.copy()
    low_temperature_predict_data = dataSet1.drop(['low_temperature'], axis=1)
    # 训练数据集
    low_temperature_train = np.array(low_temperature_predict_data)
    low_temperature_label = list_data[1]
    # 测试数据
    low_temperature_test = np.array(low_temperature_predict_data)[-1:]
    low_weather_dict = list(list_data[9].items())

    # dict_data["low_temperature_data"] = [low_temperature_train, low_temperature_test]
    # dict_data["low_temperature_labels"] = low_temperature_label
    # dict_data["low_temperature_dict"] = low_weather_dict
    # print(dict_data)
    # print("======================================================")

    # 划分预测天气状况1数据
    dataSet2 = data_set.copy()
    Weather_condition1_predict_data = dataSet2.drop(['Weather_condition1'], axis=1)
    # 训练数据集
    Weather_condition1_train = np.array(Weather_condition1_predict_data)
    Weather_condition1_label = list_data[2]
    # 测试数据
    Weather_condition1_test = np.array(Weather_condition1_predict_data)[-1:]
    Weather_condition1_dict = list(list_data[6].items())

    # dict_data["Weather_condition1_data"] = [Weather_condition1_train, Weather_condition1_test]
    # dict_data["Weather_condition1_labels"] = Weather_condition1_label
    # dict_data["Weather_condition1_dict"] = Weather_condition1_dict
    # print("======================================================")

    # 划分预测天气状况2数据
    dataSet3 = data_set.copy()
    Weather_condition2_predict_data = dataSet3.drop(['Weather_condition2'], axis=1)
    # 训练数据集
    Weather_condition2_train = np.array(Weather_condition2_predict_data)
    Weather_condition2_label = list_data[3]
    # 测试数据
    Weather_condition2_test = np.array(Weather_condition2_predict_data)[-1:]
    Weather_condition2_dict = list(list_data[7].items())

    # dict_data["Weather_condition2_data"] = [Weather_condition2_train, Weather_condition2_test]
    # dict_data["Weather_condition2_labels"] = Weather_condition2_label
    # dict_data["Weather_condition2_dict"] = Weather_condition2_dict
    # print("======================================================")

    # 划分风力风向1数据
    dataSet4 = data_set.copy()
    Wind_direction1_predict_data = dataSet4.drop(['Wind_direction1'], axis=1)
    # 训练数据集
    Wind_direction1_train = np.array(Wind_direction1_predict_data)
    Wind_direction1_label = list_data[4]
    # 测试数据
    Wind_direction1_test = np.array(Wind_direction1_predict_data)[-1:]
    Wind_direction1_dict = list(list_data[10].items())

    # dict_data["Wind_direction1_data"] = [Wind_direction1_train, Wind_direction1_test]
    # dict_data["Wind_direction1_labels"] = Wind_direction1_label
    # dict_data["Wind_direction1_dict"] = Wind_direction1_dict
    # print("======================================================")

    # 划分风力风向2数据
    dataSet5 = data_set.copy()
    Wind_direction2_predict_data = dataSet5.drop(['Wind_direction2'], axis=1)
    # 训练数据集
    Wind_direction2_train = np.array(Wind_direction2_predict_data)
    Wind_direction2_label = list_data[5]
    # 测试数据
    Wind_direction2_test = np.array(Wind_direction2_predict_data)[-1:]
    Wind_direction2_dict = list(list_data[11].items())

    # dict_data["Wind_direction2_data"] = [Wind_direction2_train, Wind_direction2_test]
    # dict_data["Wind_direction2_labels"] = Wind_direction2_label
    # dict_data["Wind_direction2_dict"] = Wind_direction2_dict
    # print(dict_data)
    # print("======================================================")

    # 预测需要使用的数据
    train_data = [high_temperature_train, low_temperature_train, Weather_condition1_train, Weather_condition2_train,
                  Wind_direction1_train, Wind_direction2_train]
    labels = [high_temperature_label, low_temperature_label, Weather_condition1_label, Weather_condition2_label,
              Wind_direction1_label, Wind_direction2_label]

    test_data = [high_temperature_test, low_temperature_test, Weather_condition1_test, Weather_condition2_test,
                 Wind_direction1_test, Wind_direction2_test]
    # print("**********今天的测试数据************")
    # print(type(test_data[0]))
    # print(test_data[0])
    # print("********************************")
    labels_list = [high_weather_dict, low_weather_dict, Weather_condition1_dict, Weather_condition2_dict,
                   Wind_direction1_dict, Wind_direction2_dict]
    # print("======================这是标签=======================")
    print(labels_list[0])
    # [('18℃', 0), ('19℃', 1), ('11℃', 2), ('8℃', 3), ('14℃', 4), ('9℃', 5), ('12℃', 6), ('15℃', 7), ('13℃', 8), ('10℃', 9), ('16℃', 10),
    #  ('17℃', 11), ('21℃', 12), ('23℃', 13), ('24℃', 14), ('25℃', 15), ('26℃', 16), ('20℃', 17), ('27℃', 18), ('22℃', 19), ('28℃', 20),
    #  ('29℃', 21), ('30℃', 22), ('31℃', 23), ('32℃', 24), ('33℃', 25), ('34℃', 26), ('35℃', 27), ('36℃', 28), ('7℃', 29), ('37℃', 30),
    #  ('6℃', 31)]
    # print("======================这是标签=======================")

    # 预测出今天的数据(类标签)
    today_data = []
    for i in range(len(train_data)):
        prediction = tree_predict(train_data[i], labels[i], test_data[i])
        # prediction 为一个列表 例如[7]
        today_data.append(prediction[0])
    # print("============today_data============")
    # print(today_data)

    # 最高温 最低温 天气状况1 天气状况2 风力风向1 风力风向2
    # 返回原来的数据（真实数据）
    today_weather = [date_days[0]]
    j = 0
    for m in labels_list:
        for n in m:
            if today_data[j] == n[1]:
                today_weather.append(n[0])
        j += 1

    # 过滤掉某个字段
    # Article.objects.defer("title")
    # 取某些字段
    # Book.objects.all().values('name','price')
    # 存数据
    # article = Article.objects.create(title='abc')

    # 存今天的数据进数据库test_data1表中
    TestData1.objects.create(high_temperature=today_data[0], low_temperature=today_data[1],
                             weather_condition1=today_data[2],
                             weather_condition2=today_data[3], wind_direction1=today_data[4],
                             wind_direction2=today_data[5])

    # 预测往后六天的数据
    six_days_num = []
    for b in range(6):
        # 调用every_col_test()函数
        result = every_col_test()
        # print(result)
        one_day = []
        for a in range(len(result)):
            # print("================")
            prediction1 = tree_predict(train_data[a], labels[a], result[a])
            # print("===============")
            one_day.append(prediction1[0])
        # 存进数据库
        TestData1.objects.create(high_temperature=one_day[0], low_temperature=one_day[1],
                                 weather_condition1=one_day[2],
                                 weather_condition2=one_day[3], wind_direction1=one_day[4],
                                 wind_direction2=one_day[5])
        six_days_num.append(one_day)

    # 找出往后六天标签对应的真实值

    next_day = TestData1.objects.all().values("high_temperature", "low_temperature", "weather_condition1",
                                              "weather_condition2", "wind_direction1", "wind_direction2")
    # 第二天
    day_data2 = [date_days[1]]
    day2 = list(list(next_day)[-1].values())
    j2 = 0
    for m2 in labels_list:
        for n2 in m2:
            if day2[j2] == n2[1]:
                day_data2.append(n2[0])
        j2 += 1

    # 第三天
    day_data3 = [date_days[2]]
    day3 = list(list(next_day)[-2].values())
    j3 = 0
    for m3 in labels_list:
        for n3 in m3:
            if day3[j3] == n3[1]:
                day_data3.append(n3[0])
        j3 += 1

    # 第四天
    day_data4 = [date_days[3]]
    day4 = list(list(next_day)[-3].values())
    j4 = 0
    for m4 in labels_list:
        for n4 in m4:
            if day4[j4] == n4[1]:
                day_data4.append(n4[0])
        j4 += 1

    # 第五天
    day_data5 = [date_days[4]]
    day5 = list(list(next_day)[-4].values())
    j5 = 0
    for m5 in labels_list:
        for n5 in m5:
            if day5[j5] == n5[1]:
                day_data5.append(n5[0])
        j5 += 1

    # 第六天
    day_data6 = [date_days[5]]
    day6 = list(list(next_day)[-5].values())
    j6 = 0
    for m6 in labels_list:
        for n6 in m6:
            if day6[j6] == n6[1]:
                day_data6.append(n6[0])
        j6 += 1

    day_data7 = [date_days[6]]
    day7 = list(list(next_day)[-6].values())
    j7 = 0
    for m7 in labels_list:
        for n7 in m7:
            if day7[j7] == n7[1]:
                day_data7.append(n7[0])
        j7 += 1

    seven_days_data = [today_weather, day_data2, day_data3, day_data4, day_data5, day_data6, day_data7]
    # seven_days_data = [today_weather, day_data2, day_data3, day_data4, day_data5, day_data6, day_data7]

    # 处理温度
    for q in seven_days_data:
        q[1] = q[1][:-1]
        q[2] = q[2][:-1]

    # print("=====7天的数据===========")
    # print(seven_days_data)
    # for zz in seven_days_data:
    #     print(zz)
    # print("===============")

    return seven_days_data


# 查询数据库
def get_img_url(name, num):
    image_data = ImageData.objects.filter(img_name__contains=name).values('img_name')
    image_address = list(image_data)[0]['img_name']
    day = "第" + str(num) + "天"
    return [day, image_address]


# 处理天气图标
def send_picture(seven_days):
    seven_images_address = {}

    for i in range(len(seven_days)):
        if '大雨' in seven_days[i][3]:
            result = get_img_url("大雨", i + 1)
        elif '暴雨' in seven_days[i][3]:
            result = get_img_url("暴雨", i + 1)
        elif '中雨' in seven_days[i][3]:
            result = get_img_url("中雨", i + 1)
        elif '小雨' in seven_days[i][3]:
            result = get_img_url("小雨", i + 1)
        elif '雷阵雨' in seven_days[i][3]:
            result = get_img_url("雷阵雨", i + 1)
        elif '阵雨' in seven_days[i][3]:
            result = get_img_url("阵雨", i + 1)
        elif '多云' in seven_days[i][3]:
            result = get_img_url("多云", i + 1)
        elif '阴' in seven_days[i][3]:
            result = get_img_url("阴", i + 1)
        elif '晴' in seven_days[i][3]:
            result = get_img_url("晴", i + 1)
        elif '雾' in seven_days[i][3]:
            result = get_img_url("雾", i + 1)
        elif '霾' in seven_days[i][3]:
            result = get_img_url("霾", i + 1)
        elif '沙尘' in seven_days[i][3]:
            result = get_img_url("沙尘", i + 1)
        elif '冰雹' in seven_days[i][3]:
            result = get_img_url("冰雹", i + 1)
        elif '小雪' in seven_days[i][3]:
            result = get_img_url("小雪", i + 1)
        elif '中雪' in seven_days[i][3]:
            result = get_img_url("中雪", i + 1)
        elif '大雪' in seven_days[i][3]:
            result = get_img_url("大雪", i + 1)
        elif '雪' in seven_days[i][3] and '雨' in seven_days[i][3]:
            result = get_img_url("雨夹雪", i + 1)
        else:
            result = get_img_url("温度计", i + 1)
        seven_images_address[result[0]] = result[1]

    return seven_images_address


def get_tips1(weather_info):
    month = int(weather_info[0][5:7])
    max_temp = int(weather_info[1])
    mini_temp = int(weather_info[2])
    wea_cond1 = weather_info[3]
    wea_cond2 = weather_info[4]
    wind_dire = weather_info[5]
    # print(month, max_temp, mini_temp, wea_cond1, wea_cond2, wind_dire)
    # -------------- 天气舒适度
    comfort_index = ['1、极不适应、35',
                     '2、很不舒适、30',
                     '3、不舒适、25',
                     '4、较舒适、22',
                     '5、舒适、20',
                     '6、较舒适、15',
                     '7、不舒适、10',
                     '8、很不舒适、8',
                     '9、极不舒适、4']

    def get_comfIndex(comfort_index, max_temp, mini_temp):
        # 4 很热，极不适应 热调节功能障碍
        if max_temp >= 35:
            comf = comfort_index[0].split('、')[1]
        #  3 热，很不舒适 过度出汗
        if max_temp >= 30 and max_temp < 35:
            comf = comfort_index[1].split('、')[1]
        #  2  暖，不舒适 出汗 、25
        if max_temp >= 25 and max_temp < 30:
            comf = comfort_index[2].split('、')[1]
        #  1 温暖，较舒适 轻度出汗，血管舒张
        if max_temp >= 22 and max_temp < 25:
            comf = comfort_index[3].split('、')[1]
        # 0 舒适，最可接受 中性
        if max_temp >= 20 and max_temp < 22:
            comf = comfort_index[4].split('、')[1]
        # -1 凉爽，较舒适 血管收缩
        if max_temp >= 15 and max_temp < 20:
            comf = comfort_index[5].split('、')[1]
        # -2 凉，不舒适 血管收缩
        if mini_temp >= 10 and max_temp < 15:
            comf = comfort_index[6].split('、')[1]
            # -3 冷，很不舒适 稍有体温下降
        if mini_temp < 9 and mini_temp >= 5:
            comf = comfort_index[7].split('、')[1]
            # -4 很冷，极不适应 发抖
        if mini_temp < 5:
            comf = comfort_index[8].split('、')[1]
        return comf

    # -------------------  洗车气象指数
    carWashing_index = ['1、适合洗车',
                        '2、不适合洗车']

    def get_carWashingIndex(carWashing_index, wea_cond1, wea_cond2):
        '''获取汽车气象指数'''
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            return carWashing_index[1].split('、')[1]
        else:
            return carWashing_index[0].split('、')[1]

    # -------------------- 穿衣气象指数
    wear_index = ['1、适合短袖、夏',
                  '2、可加件薄外套、春，秋',
                  '3、适合棉服，羽绒服类、冬']

    def get_wearIndex(wear_index, month):
        if month > 6 and month < 10:
            return wear_index[0].split('、')[1]
        elif month > 10 or month < 3:
            return wear_index[-1].split('、')[1]
        else:
            return wear_index[1].split('、')[1]

    # -------------------- 运动指数
    sport_index = ['1、适宜运动',
                   '2、较适宜运动',
                   '3、较不适宜运动',
                   '4、非常不适宜运动']

    def get_sportIndex(sport_index, max_temp, mini_temp, wea_cond1, wea_cond2):
        if max_temp > 35 or wea_cond1.find('雪') != -1 or wea_cond1.find('雨') != -1 or wea_cond2.find(
                '雪') != -1 or wea_cond2.find('雨') != -1:
            sportIndex = sport_index[-1].split('、')[1]
        if wea_cond1.find('云') != -1 or wea_cond2.find('云') != -1:
            sportIndex = sport_index[0].split('、')[1]
        if wea_cond1.find('晴') != -1 or wea_cond2.find('晴') != -1:
            sportIndex = sport_index[1].split('、')[1]
        if mini_temp < 10:
            sportIndex = sport_index[1].split('、')[1]
        return sportIndex

    # ------------------- 旅游指数分为5级，级数越高，越不适应旅游。
    travel_index = ['1、非常适宜旅游',
                    '2、适宜旅游',
                    '3、较适宜旅游',
                    '4、较不适宜旅游',
                    '5、非常不适宜旅游']

    def get_travelIndex(travel_index, max_temp, mini_temp, wea_cond1, wea_cond2):
        if max_temp < 30 and mini_temp > 10:
            # 有雨的天气 非常不适合旅游
            if wea_cond1.find('雨') != -1 and wea_cond2.find('雨') != -1:
                traverlIndex = travel_index[-1].split('、')[1]
                return traverlIndex
            # 晴天 较适合旅游
            if wea_cond1.find('晴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[0].split('、')[1]
                return traverlIndex
            # 多云 适合旅游
            if wea_cond1.find('云') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('云') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[1].split('、')[1]
                return traverlIndex
            if wea_cond1.find('阴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('阴') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[2].split('、')[1]
                return traverlIndex

        # 高温，低温天气不适合旅游
        if max_temp > 35 or mini_temp < 2:
            traverlIndex = travel_index[-1].split('、')[1]
        else:
            traverlIndex = travel_index[-2].split('、')[1]

        return traverlIndex

    # ---------------------------- 紫外线指数
    ultravioletRays_index = ['1、紫外线较弱、阴或雨天',
                             '2、 紫外线弱、多云',
                             '3、紫外线弱、少云',
                             '4、紫外线强、晴天无云',
                             '5、紫外线较强、夏季晴日']

    def get_ultravioletRaysIndex(ultravioletRays_index, month, wea_cond1, wea_cond2):
        if month > 6 and month < 10:
            # 指数值为：10～12、夏季晴日
            if wea_cond1.find('晴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                    '雨') == -1:
                ultravioletRaysIndex = ultravioletRays_index[-1].split('、')[1]
            else:
                ultravioletRaysIndex = ultravioletRays_index[-2].split('、')[1]
        # 指数值为：0～2、阴或雨天
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            ultravioletRaysIndex = ultravioletRays_index[0].split('、')[1]
            # 指数值为：7～9、晴天无云
        if wea_cond1.find('晴') != -1 and wea_cond2.find('云') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                '云') == -1:
            ultravioletRaysIndex = ultravioletRays_index[-2].split('、')[1]
        # 指数值为：5～6、少云
        if wea_cond1.find('云') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('云') != -1 and wea_cond1.find(
                '雨') == -1:
            ultravioletRaysIndex = ultravioletRays_index[1].split('、')[1]
        # 指数值为：3～4、多云
        if wea_cond1.find('云') != -1 and wea_cond2.find('云') != -1:
            ultravioletRaysIndex = ultravioletRays_index[2].split('、')[1]
        return ultravioletRaysIndex

    # ----------------------- 化妆指数
    makeup_index = ['1、建议涂点防嗮、晴，多云,阴',
                    '2、可不凃防嗮、雨']

    def get_makeUpIndex(makeup_index, month, wea_cond1, wea_cond2):
        if month > 6 and month < 10:
            if wea_cond1.find('雨') != -1 and wea_cond2.find('雨') != -1:
                return makeup_index[1].split('、')[1]
            else:
                return makeup_index[0].split('、')[1]
        else:
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                return makeup_index[1].split('、')[1]

    # ---------------------交通指数
    traffic_index = ['1、交通畅通、晴',
                     '2、交通基本畅通、云，阴',
                     '3、交通轻度拥堵、雨',
                     '4、交通中度拥堵、大雨',
                     '5、交通严重拥堵、暴雨']

    def get_trafficIndex(traffic_index, wea_cond1, wea_cond2):
        # 0～2(畅通)、晴
        if wea_cond1.find('晴') != -1 and wea_cond2.find('晴'):
            return traffic_index[0].split('、')[1]
        # 2～4(基本畅通)、云，阴
        if wea_cond1.find('云') != -1 and wea_cond2.find('云') or wea_cond1.find('阴') != -1 and wea_cond2.find('阴') != -1:
            return traffic_index[1].split('、')[1]
        # 5、8～10(严重拥堵)、暴雨
        if wea_cond1.find('暴雨') != -1 or wea_cond2.find('暴雨') != -1:
            return traffic_index[-1].split('、')[1]
        # 6～8(中度拥堵)、大雨
        if wea_cond1.find('大雨') != -1 or wea_cond2.find('大雨') != -1:
            return traffic_index[-2].split('、')[1]
        # 4～6(轻度拥堵)、雨
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            return traffic_index[2].split('、')[1]
        # 无雨天气 基本顺畅
        if wea_cond1.find('雨') == -1 or wea_cond2.find('雨') == -1:
            return traffic_index[1].split('、')[1]

    comf = get_comfIndex(comfort_index, max_temp, mini_temp)
    cw = get_carWashingIndex(carWashing_index, wea_cond1, wea_cond2)
    drsg = get_wearIndex(wear_index, month)
    sport = get_sportIndex(sport_index, max_temp, mini_temp, wea_cond1, wea_cond2)
    trav = get_travelIndex(travel_index, max_temp, mini_temp, wea_cond1, wea_cond2)
    uv = get_ultravioletRaysIndex(ultravioletRays_index, month, wea_cond1, wea_cond2)
    mu = get_makeUpIndex(makeup_index, month, wea_cond1, wea_cond2)
    ptfc = get_trafficIndex(traffic_index, wea_cond1, wea_cond2)

    tips_dict = {}
    tips_dict['comf'] = comf
    tips_dict['cw'] = cw
    tips_dict['drsg'] = drsg
    tips_dict['sport'] = sport
    tips_dict['trav'] = trav
    tips_dict['uv'] = uv
    tips_dict['mu'] = mu
    tips_dict['ptfc'] = ptfc

    # -------------------------------------- 汤的推荐 -------- -------------------

    soupSet = pd.read_excel('D:\课\小学期\小提示和汤的源码及相关数据\小提示和汤的源码及相关数据\soup.xlsx')
    springSoup = soupSet['春季'].dropna().tolist()
    summerSoup = soupSet['夏季'].dropna().tolist()
    autumnSoup = soupSet['秋季'].dropna().tolist()
    winterSoup = soupSet['冬季'].dropna().tolist()

    def get_soup(month):
        # 阳历3～5月为春季，
        if month > 2 and month < 6:
            soup = random.sample(springSoup, 1)[0]
        # 6～8月为夏季，
        elif month > 5 and month < 9:
            soup = random.sample(summerSoup, 1)[0]
        # 9～11月为秋季，
        elif month > 8 and month < 12:
            soup = random.sample(autumnSoup, 1)[0]
        # 12月～来年2月为冬季
        elif month == 12 or month < 3:
            soup = random.sample(winterSoup, 1)[0]
        return soup

    soupDict = {}
    soup = get_soup(month)
    soupInfo = soup.split('、', 2)
    soupDict['soupName'] = soupInfo[1]  # 汤名
    soupDict['soupFunction'] = soupInfo[2]  # 汤的功能
    soupDict['imgName'] = soupInfo[1].strip() + '.jpg'  # 图像的名称

    # ----------------------------------------------------------------

    # 雨雪天交替规则
    trafficTips_RainAndSnow = [
        '1、集中精神，安全礼让，速度适中，前、后、左、右都有安全车距。',
        '2、起步、行车要合理使用档位，慢抬离合、轻加油、平稳起步。',
        '3、不超载、不超速、不超车、不空档滑行。',
        '4、双手稳握方向盘，轻(慢)打方向，车辆尽量直行，轻踩刹车。',
        '5、严禁突然加油、收油、猛打方向、猛踏刹车。'
        '6、车辆如遇侧滑或跑偏，及时减油，往侧滑方打轮，轻点刹车，以调正车身。',
        '7、坡路行车，常备三角木。',
        '8、突遇事故发生，踏死刹车不松开。',
        '9、驾驶尽量远离自行车，以防其滑倒发生事故。',
        '10、雪后阳光眩目时，尽量带防护镜。',
        '12、白天、下雪天开车要打开雾灯。',
        '13、路面如有冰凌、雪凌，不要超车和变道。']

    # 台风天气注意
    TyphoonDay_attension = [
        '1、时刻留意台风动向，注意收听、收看媒体报道或通过气象网站等，了解台风的最新情况，注意查看突发紧急状况的信息。',
        '2、台风来之前要先关好门窗，可在窗玻璃上用胶布贴成“米”字图形，以防窗玻璃破碎。',
        '3、家中阳台上花盆等易受大风影响的室外物品要摆放、固定妥当。避免刮台风的时候，把盆栽刮落，砸伤路人，造成不必要的人身安全威胁。',
        '4、准备好相关食物。方便面、面包、水、蜡烛、手电筒、充电宝、手机、ipad等相关物品要准备好，防止停水停电的情况出现。',
        '5、不能居住旧房子。旧房子很容易受到台风的影响而倒塌，这样是很危险的。所以如果房子比较破旧的话，最好暂时找一个比较安全的地方住一下，避免因房子倒塌造成生命危险。',
        '6、提前加固房子周围容易被吹到的物品。加固围板、棚架、广告牌等易被风吹动的搭建物，还有周围的树木，这些东西如果不加固好，被风吹走或倒了都很有可能砸伤路人，因此也要格外注意。',
        '7、保持视野良好，缓慢行驶，要留意周围环境，不要盲目涉水，防止行车撞人',
        '8、台风过后需要注意环境卫生，及时清理垃圾。如果有食物被水淹过，或者有用品在台风中受损，也要及时清理。避免滋生细菌或各种疫病。',
        '9、注意饮食的安全。不吃腐败变质食物，不吃苍蝇叮爬过的食物，不吃未洗净的瓜果等；防止皮肤直接接触疫水，如有外出要穿胶鞋等。',
        '10、不要忘记灾后防疫。家里的饮用水如受到污染，要进行消毒，同时还要做好周围环境的打扫工作，被淹或者被雨水浸渍的地方清洗时最好喷洒些消毒药水。',
        '11、走在路上要尽量避免一些危险物品。如发现高压线铁塔倾倒、电线低垂或断折，千万不要接近，更不要用手去触摸，因为这极易引发触电事故。',
        '12、不要盲目开车进山。经过暴雨的冲刷，山区山石塌方、路基被毁等灾害的发生几率增加，此时进山危险很大。'
    ]

    # 高温天气
    High_temperature_tips = [
        '1、在户外工作要带好防护设备，防止灼伤。',
        '2、尽量不要在一天中气温最高、阳光直射的时候进行户外活动。',
        '3、高温天气，饮食上以清淡、爽口的食物为主，可以多喝一些清凉饮品，如绿豆汤等。此外不要吃过多的辣味、油腻食品，防止上火和身体不适。',
        '4、可以进行室内通风、吹吹风扇和空调、喝一些冷饮等，防止中暑。',
        '5、高温天气条件下进行工作和生活，一定要注意度的把握，不可以过度劳累，尤其是在中午时候要放下工作，进行及时午休',
        '6、外出游泳要注意安全，结伴游泳，时间不宜过长，防止劳累引发胸闷、身体无力等症状',
        '7、注意对老人儿童，残疾人的关怀，配备一些痱子粉、蚊帐、驱蚊药品等']

    tips = pd.read_excel('D:\课\小学期\小提示和汤的源码及相关数据\小提示和汤的源码及相关数据\温馨提示.xlsx')
    data = tips['描述'].tolist()

    def get_weatherTip(month, max_temp, mini_temp, wea_cond1, wea_cond2, wind_dire):
        spring_rain_lst, spring_wind_lst, spring_wind_rain_lst, spring_lst = [], [], [], []  # 春天
        summer_rain_lst, summer_wind_lst, summer_wind_rain_lst, summer_lst = [], [], [], []  # 夏天
        winter_rain_lst, winter_wind_lst, winter_wind_rain_lst, winter_lst = [], [], [], []  # 冬天
        autumn_rain_lst, autumn_wind_lst, autumn_wind_rain_lst, autumn_lst = [], [], [], []  # 冬天

        for d in data:
            # 阳历3～5月为春季，
            if month > 2 and month < 6:
                if d.find('春') != -1:
                    # 春天，下雨天
                    if d.find('雨') != -1:
                        spring_rain_lst.append(d)
                        # 春天，刮风天
                    if d.find('雨') != -1 and d.find('风') == -1:
                        spring_wind_lst.append(d)
                    # 春天，下雨，刮风天
                    if d.find('雨') != -1 and d.find('风') != -1:
                        spring_wind_rain_lst.append(d)
                    else:
                        spring_lst.append(d)
            # 6～8月为夏季，
            elif month > 5 and month < 9:
                if d.find('夏') != -1 or d.find('高温') != -1 or d.find('暑') != -1 or d.find('七月') != -1 or d.find(
                        '热') != -1:
                    # 夏天，下雨天
                    if d.find('雨') != -1:
                        summer_rain_lst.append(d)
                        # 夏天，刮风天
                    if d.find('雨') != -1 and d.find('风') == -1:
                        summer_wind_lst.append(d)
                    # 夏天，下雨，刮风天
                    if d.find('雨') != -1 and d.find('风') != -1:
                        summer_wind_rain_lst.append(d)
                    else:
                        summer_lst.append(d)
            # 9～11月为秋季，
            elif month > 8 and month < 12:
                if d.find('秋') != -1 or d.find('凉爽') != -1:
                    # 秋天，下雨天
                    if d.find('雨') != -1:
                        autumn_rain_lst.append(d)
                        # 夏天，刮风天
                    if d.find('雨') != -1 and d.find('风') == -1:
                        autumn_wind_lst.append(d)
                    # 秋天，下雨，刮风天
                    if d.find('雨') != -1 and d.find('风') != -1:
                        autumn_wind_rain_lst.append(d)
                    else:
                        autumn_lst.append(d)

            # 12月～来年2月为冬季
            elif month == 12 or month < 3:
                # 冬天
                if d.find('北风') != -1 or d.find('冬') != -1 or d.find('雪') != -1 or d.find('低温') != -1:
                    # 冬天，下雨天
                    if d.find('雨') != -1:
                        winter_rain_lst.append(d)
                        # 冬天，下雨，不刮风天
                    if d.find('雨') != -1 and d.find('风') == -1:
                        winter_wind_lst.append(d)
                    # 冬天，下雨，刮风天
                    if d.find('雨') != -1 and d.find('风') != -1:
                        winter_wind_rain_lst.append(d)
                    else:
                        winter_rain_lst.append(d)
        # 高温无雨天气
        if max_temp > 35 and wea_cond1.find('雨') == -1 and wea_cond2.find('雨') == -1:
            return random.sample(High_temperature_tips, 1)[0].split('、', 1)[1]

        # 台风天气注意
        if wea_cond1.find('台风') != -1 or wea_cond2.find('台风') != -1:
            return random.sample(TyphoonDay_attension, 1)[0].split('、', 1)[1]

        # 雨雪天交替规则
        if wea_cond1.find('雨') != -1 and wea_cond2.find('雪') != -1 or wea_cond2.find('雨') != -1 and wea_cond1.find(
                '雪') != -1:
            return random.sample(trafficTips_RainAndSnow, 1)[0].split('、', 1)[1]

        # 春天
        if month > 2 and month < 6:
            # 春天，下雨天
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                temp = random.sample(spring_rain_lst, 1)[0].split('、', 1)[1]
                # 春天，刮风天
            if wind_dire.find('风') != -1:
                temp = random.sample(spring_wind_lst, 1)[0].split('、', 1)[1]
                # 春天，下雨，刮风天
            if wea_cond1.find('雨') != -1 and wind_dire.find('风') != -1 or wea_cond2.find('雨') != -1 and wind_dire.find(
                    '风') != -1:
                temp = random.sample(spring_wind_rain_lst, 1)[0].split('、', 1)[1]
            else:
                temp = random.sample(spring_lst, 1)[0].split('、', 1)[1]
            return temp

        # 6～8月为夏季，
        elif month > 5 and month < 9:
            # 夏天，下雨天
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                temp = random.sample(summer_rain_lst, 1)[0].split('、', 1)[1]
                # 夏天，刮风天
            if wind_dire.find('风') != -1:
                temp = random.sample(summer_wind_lst, 1)[0].split('、', 1)[1]
                # 夏天，下雨，刮风天
            if wea_cond1.find('雨') != -1 and wind_dire.find('风') != -1 or wea_cond2.find('雨') != -1 and wind_dire.find(
                    '风') != -1:
                temp = random.sample(summer_wind_rain_lst, 1)[0].split('、', 1)[1]
            else:
                temp = random.sample(summer_lst, 1)[0].split('、', 1)[1]
            return temp

            # 9～11月为秋季，
        elif month > 8 and month < 12:
            # 秋天，下雨天
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                temp = random.sample(autumn_rain_lst, 1)[0].split('、', 1)[1]
                # 秋天，下雨，刮风天
            if wea_cond1.find('雨') != -1 and wind_dire.find('风') != -1 or wea_cond2.find('雨') != -1 and wind_dire.find(
                    '风') != -1:
                temp = random.sample(autumn_wind_rain_lst, 1)[0].split('、', 1)[1]
            else:
                temp = random.sample(autumn_lst, 1)[0].split('、', 1)[1]
            return temp

        # 12月～来年2月为冬季
        elif month == 12 or month < 3:
            # 冬天，下雨天
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                temp = random.sample(winter_rain_lst, 1)[0].split('、', 1)[1]
                # 冬天，刮风天
            if wind_dire.find('风') != -1:
                temp = random.sample(winter_wind_lst, 1)[0].split('、', 1)[1]
                # 冬天，下雨，刮风天
            if wea_cond1.find('雨') != -1 and wind_dire.find('风') != -1 or wea_cond2.find('雨') != -1 and wind_dire.find(
                    '风') != -1:
                temp = random.sample(winter_wind_rain_lst, 1)[0].split('、', 1)[1]
            else:
                temp = random.sample(winter_lst, 1)[0].split('、', 1)[1]
            return temp

    tips_dict['weatherTip'] = get_weatherTip(month, max_temp, mini_temp, wea_cond1, wea_cond2, wind_dire)
    return tips_dict, soupDict



# 获取温馨小提示
def get_tips(weather_info):
    month = int(weather_info[0][5:7])
    max_temp = int(weather_info[1])
    mini_temp = int(weather_info[2])
    wea_cond1 = weather_info[3]
    wea_cond2 = weather_info[4]
    wind_dire = weather_info[5]
    print(month, max_temp, mini_temp, wea_cond1, wea_cond2, wind_dire)
    # -------------- 天气舒适度
    comfort_index = ['1、极不适应、35',
                     '2、很不舒适、30',
                     '3、不舒适、25',
                     '4、较舒适、22',
                     '5、舒适、20',
                     '6、较舒适、15',
                     '7、不舒适、10',
                     '8、很不舒适、8',
                     '9、极不适应、4']

    def get_comfIndex(comfort_index, max_temp, mini_temp):
        # 4 很热，极不适应 热调节功能障碍
        if max_temp >= 35:
            comf = comfort_index[0].split('、')[1]
        #  3 热，很不舒适 过度出汗
        if max_temp >= 30 and max_temp < 35:
            comf = comfort_index[1].split('、')[1]
        #  2  暖，不舒适 出汗 、25
        if max_temp >= 25 and max_temp < 30:
            comf = comfort_index[2].split('、')[1]
        #  1 温暖，较舒适 轻度出汗，血管舒张
        if max_temp >= 22 and max_temp < 25:
            comf = comfort_index[3].split('、')[1]
        # 0 舒适，最可接受 中性
        if max_temp >= 20 and max_temp < 22:
            comf = comfort_index[4].split('、')[1]
        # -1 凉爽，较舒适 血管收缩
        if max_temp >= 15 and max_temp < 20:
            comf = comfort_index[5].split('、')[1]
        # -2 凉，不舒适 血管收缩
        if mini_temp >= 10 and max_temp < 15:
            comf = comfort_index[6].split('、')[1]
            # -3 冷，很不舒适 稍有体温下降
        if mini_temp < 9 and mini_temp >= 5:
            comf = comfort_index[7].split('、')[1]
            # -4 很冷，极不适应 发抖
        if mini_temp < 5:
            comf = comfort_index[8].split('、')[1]
        return comf

    # -------------------  洗车气象指数
    carWashing_index = ['1、适合',
                        '2、不适合']

    def get_carWashingIndex(carWashing_index, wea_cond1, wea_cond2):
        '''获取汽车气象指数'''
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            return carWashing_index[1].split('、')[1]
        else:
            return carWashing_index[0].split('、')[1]

    # -------------------- 穿衣气象指数
    wear_index = ['1、适合衬衫、夏',
                  '2、可加件外套、春，秋',
                  '3、适合棉服，羽绒服类、冬']

    def get_wearIndex(wear_index, month):
        if month > 6 and month < 10:
            return wear_index[0].split('、')[1]
        elif month > 10 or month < 3:
            return wear_index[-1].split('、')[1]
        else:
            return wear_index[1].split('、')[1]

    # -------------------- 运动指数
    sport_index = ['1、适宜',
                   '2、较适宜',
                   '3、较不适宜',
                   '4、非常不适宜']

    def get_sportIndex(sport_index, max_temp, mini_temp, wea_cond1, wea_cond2):
        if max_temp > 35 or wea_cond1.find('雪') != -1 or wea_cond1.find('雨') != -1 or wea_cond2.find(
                '雪') != -1 or wea_cond2.find('雨') != -1:
            sportIndex = sport_index[-1].split('、')[1]
        if wea_cond1.find('云') != -1 or wea_cond2.find('云') != -1:
            sportIndex = sport_index[0].split('、')[1]
        if wea_cond1.find('晴') != -1 or wea_cond2.find('晴') != -1:
            sportIndex = sport_index[1].split('、')[1]
        if mini_temp < 10:
            sportIndex = sport_index[1].split('、')[1]
        return sportIndex

    # ------------------- 旅游指数分为5级，级数越高，越不适应旅游。
    travel_index = ['1、非常适宜',
                    '2、适宜',
                    '3、较适宜',
                    '4、较不适宜',
                    '5、非常不适宜']

    def get_travelIndex(travel_index, max_temp, mini_temp, wea_cond1, wea_cond2):
        if max_temp < 30 and mini_temp > 10:
            # 有雨的天气 非常不适合旅游
            if wea_cond1.find('雨') != -1 and wea_cond2.find('雨') != -1:
                traverlIndex = travel_index[-1].split('、')[1]
                return traverlIndex
            # 晴天 较适合旅游
            if wea_cond1.find('晴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[0].split('、')[1]
                return traverlIndex
            # 多云 适合旅游
            if wea_cond1.find('云') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('云') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[1].split('、')[1]
                return traverlIndex
            if wea_cond1.find('阴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('阴') != -1 and wea_cond1.find(
                    '雨') == -1:
                traverlIndex = travel_index[2].split('、')[1]
                return traverlIndex

        # 高温，低温天气不适合旅游
        if max_temp > 35 or mini_temp < 2:
            traverlIndex = travel_index[-1].split('、')[1]
        else:
            traverlIndex = travel_index[-2].split('、')[1]

        return traverlIndex

    # ---------------------------- 紫外线指数
    ultravioletRays_index = ['1、紫外线较弱、阴或雨天',
                             '2、 紫外线弱、多云',
                             '3、紫外线弱、少云',
                             '4、紫外线强、晴天无云',
                             '5、紫外线较强、夏季晴日']

    def get_ultravioletRaysIndex(ultravioletRays_index, month, wea_cond1, wea_cond2):
        if month > 6 and month < 10:
            # 指数值为：10～12、夏季晴日
            if wea_cond1.find('晴') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                    '雨') == -1:
                ultravioletRaysIndex = ultravioletRays_index[-1].split('、')[1]
            else:
                ultravioletRaysIndex = ultravioletRays_index[-2].split('、')[1]
        # 指数值为：0～2、阴或雨天
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            ultravioletRaysIndex = ultravioletRays_index[0].split('、')[1]
            # 指数值为：7～9、晴天无云
        if wea_cond1.find('晴') != -1 and wea_cond2.find('云') == -1 or wea_cond2.find('晴') != -1 and wea_cond1.find(
                '云') == -1:
            ultravioletRaysIndex = ultravioletRays_index[-2].split('、')[1]
        # 指数值为：5～6、少云
        if wea_cond1.find('云') != -1 and wea_cond2.find('雨') == -1 or wea_cond2.find('云') != -1 and wea_cond1.find(
                '雨') == -1:
            ultravioletRaysIndex = ultravioletRays_index[1].split('、')[1]
        # 指数值为：3～4、多云
        if wea_cond1.find('云') != -1 and wea_cond2.find('云') != -1:
            ultravioletRaysIndex = ultravioletRays_index[2].split('、')[1]
        return ultravioletRaysIndex

    # ----------------------- 化妆指数
    makeup_index = ['1、建议涂点防嗮、晴，多云,阴',
                    '2、可不凃防嗮、雨']

    def get_makeUpIndex(makeup_index, month, wea_cond1, wea_cond2):
        if month > 6 and month < 10:
            if wea_cond1.find('雨') != -1 and wea_cond2.find('雨') != -1:
                return makeup_index[1].split('、')[1]
            else:
                return makeup_index[0].split('、')[1]
        else:
            if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
                return makeup_index[1].split('、')[1]

    # ---------------------交通指数
    traffic_index = ['1、畅通、晴',
                     '2、基本畅通、云，阴',
                     '3、轻度拥堵、雨',
                     '4、中度拥堵、大雨',
                     '5、严重拥堵、暴雨']

    def get_trafficIndex(traffic_index, wea_cond1, wea_cond2):
        # 0～2(畅通)、晴
        if wea_cond1.find('晴') != -1 and wea_cond2.find('晴'):
            return traffic_index[0].split('、')[1]
        # 2～4(基本畅通)、云，阴
        if wea_cond1.find('云') != -1 and wea_cond2.find('云') or wea_cond1.find('阴') != -1 and wea_cond2.find('阴') != -1:
            return traffic_index[1].split('、')[1]
        # 5、8～10(严重拥堵)、暴雨
        if wea_cond1.find('暴雨') != -1 or wea_cond2.find('暴雨') != -1:
            return traffic_index[-1].split('、')[1]
        # 6～8(中度拥堵)、大雨
        if wea_cond1.find('大雨') != -1 or wea_cond2.find('大雨') != -1:
            return traffic_index[-2].split('、')[1]
        # 4～6(轻度拥堵)、雨
        if wea_cond1.find('雨') != -1 or wea_cond2.find('雨') != -1:
            return traffic_index[2].split('、')[1]
        # 无雨天气 基本顺畅
        if wea_cond1.find('雨') == -1 or wea_cond2.find('雨') == -1:
            return traffic_index[1].split('、')[1]

    comf = get_comfIndex(comfort_index, max_temp, mini_temp)
    cw = get_carWashingIndex(carWashing_index, wea_cond1, wea_cond2)
    drsg = get_wearIndex(wear_index, month)
    sport = get_sportIndex(sport_index, max_temp, mini_temp, wea_cond1, wea_cond2)
    trav = get_travelIndex(travel_index, max_temp, mini_temp, wea_cond1, wea_cond2)
    uv = get_ultravioletRaysIndex(ultravioletRays_index, month, wea_cond1, wea_cond2)
    mu = get_makeUpIndex(makeup_index, month, wea_cond1, wea_cond2)
    ptfc = get_trafficIndex(traffic_index, wea_cond1, wea_cond2)

    tips_dict = {}
    tips_dict['comf'] = comf
    tips_dict['cw'] = cw
    tips_dict['drsg'] = drsg
    tips_dict['sport'] = sport
    tips_dict['trav'] = trav
    tips_dict['uv'] = uv
    tips_dict['mu'] = mu
    tips_dict['ptfc'] = ptfc

    return tips_dict


# 获取预测结果
def get_city(request):
    # print("================小恒给范德萨发的咖啡和的撒+++++++++++++++=")
    # m_model = GuangzhouWeather
    m_models = [GuangzhouWeather, DongguangWeather, FoshanWeather, ZhuhaiWeather, ShenzhenWeather, HuizhouWeather,
                MaomingWeather, ZhanjiangWeather,
                JiangmenWeather, ShantouWeather, ShaoguanWeather, ZhaoqingWeather, ZhongshanWeather]

    cities = ["guangzhou", "dongguang", "foshan", "zhuhai", "shenzhen",
              "huizhou", "maoming", "zhanjiang",
              "jiangmen", "shantou", "shaoguan", "zhaoqing", "zhongshan"]

    keys = ["广州", "东莞", "佛山", "珠海", "深圳",
            "惠州", "茂名", "湛江",
            "江门", "汕头", "韶关", "肇庆", "中山"]

    # 遍历所有的表
    context = {}
    for i in range(len(m_models)):
        # 调用 生成csv文件
        get_data1(m_models[i])
        # 调用
        result = data_predict()
        # 获取今天的天气情况
        # 去掉风力风向2

        # today_weather = today_condiction(cities[i])[:-1]
        # print(today_weather)

        # tips = get_tips(today_weather)
        # result.append(today_weather)

        tips = get_tips1(result[0])

        # 返回图标
        img_address = send_picture(result)
        context[keys[i]] = result
        context[keys[i] + '_img_address'] = img_address
        context[keys[i] + "_tips"] = tips

        # 删除表的所有数据
        TestData1.objects.all().delete()
    return JsonResponse(context)


# 保存图片地址到数据库
# def save_img_address(request):
#     img_path = 'D:\课\小学期\天气ui\天气ui'
#     img_name_list = os.listdir(img_path)
#     # print(img_name_list)
#     for img_name in img_name_list:
#         img_full_path = os.path.join(img_path, img_name)
#         ImageData.objects.create(img_name=img_full_path)
#     return HttpResponse("成功")

def index(request):
    # 删除8月份的数据
    data = TestData1.objects.all()
    data.delete()
    return HttpResponse("成功")
