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

    return today_weather


# 各个字段的测试数据
def every_col_test():
    # 预测明天的数据
    # col_names = ['high_temperature', 'low_temperature', 'weather_condition1', 'weather_condition2', 'wind_direction1','wind_direction2']
    high_temperature_test = TestData1.objects.all().values('low_temperature', 'weather_condition1',
                                                           'weather_condition2', 'wind_direction1', 'wind_direction2')
    high_temperature_test = list(list(high_temperature_test)[-1].values())
    print("=======转化=========")
    print(high_temperature_test)

    low_temperature_test = TestData1.objects.all().values('high_temperature', 'weather_condition1',
                                                          'weather_condition2', 'wind_direction1', 'wind_direction2')
    low_temperature_test = list(list(low_temperature_test)[-1].values())
    print(low_temperature_test)
    print("================")

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
    print("**********明天测试数据**************")
    print(type(result[0]))
    print(result[0])
    print("*******************************")
    print(len(result))
    return result


# 预测数据
def data_predict():
    # 一周的时间
    today = datetime.date.today()
    date_days = [today]
    for d in range(1, 7):
        futrue_day = today + datetime.timedelta(days=d)
        date_days.append(futrue_day)

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
    print("**********今天的测试数据************")
    print(type(test_data[0]))
    print(test_data[0])
    print("********************************")
    labels_list = [high_weather_dict, low_weather_dict, Weather_condition1_dict, Weather_condition2_dict,
                   Wind_direction1_dict, Wind_direction2_dict]
    print("======================这是标签=======================")
    print(labels_list[0])
    # [('18℃', 0), ('19℃', 1), ('11℃', 2), ('8℃', 3), ('14℃', 4), ('9℃', 5), ('12℃', 6), ('15℃', 7), ('13℃', 8), ('10℃', 9), ('16℃', 10),
    #  ('17℃', 11), ('21℃', 12), ('23℃', 13), ('24℃', 14), ('25℃', 15), ('26℃', 16), ('20℃', 17), ('27℃', 18), ('22℃', 19), ('28℃', 20),
    #  ('29℃', 21), ('30℃', 22), ('31℃', 23), ('32℃', 24), ('33℃', 25), ('34℃', 26), ('35℃', 27), ('36℃', 28), ('7℃', 29), ('37℃', 30),
    #  ('6℃', 31)]
    print("======================这是标签=======================")

    # 预测出今天的数据(类标签)
    today_data = []
    for i in range(len(train_data)):
        prediction = tree_predict(train_data[i], labels[i], test_data[i])
        # prediction 为一个列表 例如[7]
        today_data.append(prediction[0])
    print("============today_data============")
    print(today_data)

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

    # seven_days_data = [today_weather, day_data2, day_data3, day_data4, day_data5, day_data6, day_data7]
    seven_days_data = [day_data2, day_data3, day_data4, day_data5, day_data6, day_data7]

    # 处理温度
    for q in seven_days_data:
        q[1] = q[1][:-1]
        q[2] = q[2][:-1]

    print("=====7天的数据===========")
    # print(seven_days_data)
    for zz in seven_days_data:
        print(zz)
    print("===============")

    return seven_days_data


# 扩展功能,温馨小提示
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
    print("================小恒给范德萨发的咖啡和的撒+++++++++++++++=")
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
        today_weather = today_condiction(cities[i])[:-1]
        result.append(today_weather)

        tips = get_tips(today_weather)

        context[keys[i]] = result
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
