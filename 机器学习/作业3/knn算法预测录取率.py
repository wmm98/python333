# 读文件
import pandas as pd
import operator
import numpy as np
import random
from random import shuffle


df = pd.read_csv('D:\课\机器学习\机器学习作业\作业3\作业3\Admission_Predict_Ver1.1.csv')
# 显示前5条数据
# print(df.head())
# # 数据尺寸
# print(df.shape)

# 打乱数据，选择其中的70%作为训练集，剩余的20%作为测试集
random.seed(42)
indices = np.arange(0, (df.shape[0] - 1)).tolist()
train_num = int(0.8 * df.shape[0])
shuffle(indices)
train_indices = indices[:train_num]
test_indices = indices[train_num:]
train_data = df.iloc[train_indices, :]
test_data = df.iloc[test_indices, :]
# print(train_data)
# print(test_data)

# 训练集数据和标签
D = np.array(train_data.iloc[:, :-1])
# print(D)
# L = np.array(train_data.iloc[:, -1]).astype(str)

# L = np.array(train_data.iloc[:, -1]).astype(float)
# print(L)

# 训练标签
train_Y = []
for j in np.array(train_data.iloc[:, -1]).astype(float):
    if j > 0.7:
        train_Y.append('1')
    else:
        train_Y.append("0")
L = train_Y
# print(train_Y)
# print(L)

# 测试集数据和标签
X = np.array(test_data.iloc[:, :-1])
# print(X)

# # Y = np.array(test_data.iloc[:, -1]).astype(str)
# Y = np.array(test_data.iloc[:, -1]).astype(float)
# # print(Y)

# 测试标签
test_Y = []
for i in np.array(test_data.iloc[:, -1]).astype(float):
    if i > 0.7:
        test_Y.append(str(1))
    else:
        test_Y.append(str(0))
# print(test_Y)
Y = test_Y
# print(Y)


def knnClassifier(inX, D, L, k):
    'KNN算法分类器，inX未知数据，D，L分别是数据列表和标签列表'
    # 计算距离，并排序
    D = np.array(D)
    L = np.array(L)
    [m, n] = D.shape
    differMat = np.tile(inX, (m, 1)) - D
    distanceSqur = (differMat ** 2).sum(axis=1)
    distance = distanceSqur ** 0.5
    indices = np.argsort(distance)[:k]
    votelabels = L[indices]
    # 统计标签出现的次数
    count = {}
    for label in votelabels:
        count[label] = count.get(label, 0) + 1
    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    # print(count,res)
    return res[0][0]


res = []
count = 0

for inX in X:
    res.append(knnClassifier(inX, D, L, 5))
# print(res)

# for index, predict_label in enumerate(res):
#     if predict_label == Y[index]:
#         # print(predict_label, index)
#         count += 1
for i in range(len(res)):
    if res[i] == Y[i]:
        count += 1
print("KNN算法k=5时，准确率为%.2f" % (count / len(Y)))


def autoNorm(dataSet):
    # print(dataSet)
    '归一化'
    minVals = dataSet.min(0)
    # print(minVals)
    maxVals = dataSet.max(0)
    # print(maxVals)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet

# 由于归一化特征之后准确率变低了，所以在此不需要归一化
# 归一化特征之后准确率
# res = []
# count = 0
#
# for inX in autoNorm(X):
#     res.append(knnClassifier(inX, autoNorm(D), L, 5))
#
# for index, predict_label in enumerate(res):
#     if predict_label == Y[index]:
#         count += 1
# print("归一化特征之后，KNN算法k=3时，准确率为%.2f" % (count / len(Y)))
