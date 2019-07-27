# 读文件
import pandas as pd
import operator
import numpy as np
import random
from random import shuffle


df = pd.read_csv('D:\课\机器学习\机器学习作业\作业3\作业3\Admission_Predict_Ver1.1.csv')
# 显示前5条数据
print(df.head())
# 数据尺寸
print(df.shape)

# 打乱数据，选择其中的80%作为训练集，剩余的20%作为测试集
random.seed(42)
indices = np.arange(0, (df.shape[0] - 1)).tolist()
train_num = int(0.8 * df.shape[0])
shuffle(indices)
train_indices = indices[:train_num]
test_indices = indices[train_num:]
train_data = df.iloc[train_indices, :]
test_data = df.iloc[test_indices, :]

# 训练集数据和标签
D = np.array(train_data.iloc[:, :-1])

# 训练标签
train_Y = []
for j in np.array(train_data.iloc[:, -1]).astype(float):
    if j >= 0.7:
        train_Y.append('1')
    else:
        train_Y.append("0")
L = train_Y


# 测试集数据和标签
X = np.array(test_data.iloc[:, :-1])

# 测试标签
test_Y = []
for i in np.array(test_data.iloc[:, -1]).astype(float):
    if i >= 0.7:
        test_Y.append(str(1))
    else:
        test_Y.append(str(0))
Y = test_Y


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

print("测试数据标签")
print(np.array(Y))
print("分类后的结果")
print(np.array(res))

for i in range(len(res)):
    if res[i] == Y[i]:
        count += 1
print("KNN算法k=5时，准确率为%.2f" % (count / len(Y)))




