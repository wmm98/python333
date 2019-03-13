import numpy as np
import operator

def classfier(dataSet, labels, intX, k):
    # 欧式距离的计算
    dataSetSize = dataSet.shape[0]  # 返回数组的函数
    diffMat = np.tile(intX, (dataSetSize, 1)) - dataSet  # 矩阵的减法求当前点到训练集点的差，返回的是数组
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)  # 行相加
    distance = sqDistance ** 0.5
    sortDistance = distance.argsort()  # 返回的是元素下标索引的数组
    # print(sortDistance)

    class_count = {}
    for i in range(k):
        i_labels = labels[sortDistance[i]]
        class_count[i_labels] = class_count.get(i_labels, 0) + 1

    # print(class_count)

    max_count = 0  # 计算出现次数做多的
    for k, j in class_count.items():
        if j > max_count:
            max_count = j
            classes = k
    return classes

    # 书本的按照按照值去排序
    # sortClass_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)  # 倒序
    # return sortClass_count[0][0]


f = open('D:\课\机器学习\MLcode\MLcode\machinelearninginaction\Ch02\datingTestSet.txt')
dataSet = []
labels = []
for line in f.readlines():
    line = line.strip().split("\t")
    labels.append(line[-1])
    line = list(map(float, line[:3]))
    dataSet.append(line)
    # print(line)
# print(dataSet)
# print(labels)
dataSet = np.array(dataSet)
# print(dataSet[:5])
labels = np.array(labels)
# print(labels[:5])
intX = np.array([0, 0, 0])
# print(intX)  # 表示未知的输入
k = 5
result = classfier(dataSet, labels, intX, k)
print(result)
