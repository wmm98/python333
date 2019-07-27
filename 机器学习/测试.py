import numpy as np
from math import log
import operator
import csv
from numpy import mat
import random
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np


# # 加载数据集
# def loaddataset():
#     dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
#     labels = ['no surfacing', 'flippers']
#     return dataset, labels
#
#
# D, L = loaddataset()


# 计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    #     print(shannonEnt)
    # print(labelCounts)
    # {'yes': 2, 'no': 3}
    return shannonEnt


# print(D)
# [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
# print(L)
# ['no surfacing', 'flippers']

# 计算给定数据集的香农熵
def calcuEntropy(dataSet):
    '''
    输入：列表形式数据集(最后一列为类别标签)
    输出：熵
    '''
    tar = np.array(dataSet)[:, -1]
    count = {}
    for key in tar:
        count[key] = count.get(key, 0) + 1
    entropy = 0
    for key in count:
        prob = count[key] / tar.shape[0]
        entropy += -prob * log(prob, 2)
    return entropy


# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    smallData = []
    for row in dataSet:
        if row[axis] == value:
            temp = row[:axis]
            # print(temp)
            temp.extend(row[axis + 1:])
            # print(temp)
            smallData.append(temp)
    # print(smallData)
    return smallData


# 选择最好的数据集划分方式 苏康代码
# def choosebestfeatTosplit(dataSet):
#     D = np.array(dataSet)
#     [m, n] = D.shape
#     num_feat = n - 1
#     E = np.zeros(num_feat)
#     for i in range(num_feat):
#         for value in set(D[:, i]):
#             smallData = splitDataSet(dataSet, i, int(value))
#             prob = len(smallData) / m
#             E[i] += prob * calcuEntropy(smallData)
#     return np.argsort(E)[0]


# 选择最好的数据集划分方式 书本代码
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 特征数，最后一个是分类所以要减1
    baseEntropy = calcShannonEnt(dataSet)  # 划分前的熵
    bestInfoGain = 0.0  # 信息增益
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]  # 提取低i列的所有值
        # print(featList)
        # [1, 1, 1, 0, 0]
        # [1, 1, 0, 1, 1]
        uniqueVals = set(featList)  # 通过set函数，筛选值,即集合，不含重复的值
        # print(uniqueVals)
        # {0, 1}
        # {0, 1}
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))  # 概率
            newEntropy += calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # print(classList)
    if classList.count(classList[0]) == len(classList):  # 类别完全相同
        return classList[0]
    if len(dataSet[0]) == 1:  # 特征抽取完，但类别还不完全相同
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}  # 创建节点
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:  # 划分，创建子树
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:  # 比较特征值，决策树是根据特征的值划分的
            if type(secondDict[key]).__name__ == 'dict':  # 比较是否到达叶结点
                classLabel = classify(secondDict[key], featLabels, testVec)  # 递归调用
            else:
                classLabel = secondDict[key]
    return classLabel


filename = 'D:\课\机器学习\机器学习作业\机器学习作业\heart.csv'
with open(filename) as f:
    reader = csv.reader(f)

    l = list(reader)[1:]
    # # # np.random.shuffle(l)

    result_data = []
    for i in l:
        data = []
        for j in i:
            data.append(float(j))
        result_data.append(data)
        dataset = result_data
    # dataset = np.array(result_data)
# print(dataset)
# print(len(dataset))

    # labels1 = list(reader)[:1]
    # labels = []
    # for m in labels1:
    #     for n in m[:-1]:
    #         labels.append(n)
    # print(labels)

labels = ['锘縜ge', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

myTree = createTree(dataset, labels)
print(myTree)
print(classify(myTree, labels, [63.0, 1.0, 3.0, 145.0, 233.0, 1.0, 0.0, 150.0, 0.0, 2.3, 0.0, 0.0, 1.0]))
# print(dataset[:1])

