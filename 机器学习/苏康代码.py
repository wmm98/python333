import numpy as np
from numpy import mat


def loadDataSet(filename):
    dataMat = []
    labelMat = []
    numFeat = len(open(filename).readline().split('\t')) - 1
    # print(numFeat)
    # print(numFeat[:5])
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        # print(curLine[:5])
        # print(curLine)
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def standReges(XArr, yArr):
    XMat = mat(XArr)
    # print(XMat[:, 1])
    # print(XMat)
    yMat = mat(yArr).T
    # print(yMat[:, 0])
    # print(yArr)
    # print(mat(yArr))
    # print(yMat)
    XTX = XMat.T * XMat
    # print(XTX)
    if np.linalg.det(XTX) == 0.0:
        print("This matrix is singular,cannot do inverse")
        return
    Ws = XTX.I * XMat.T * yMat
    return Ws


D, L = loadDataSet('D:\课\机器学习\linear_regression\linear_regression\ex0.txt')
# D = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
# L = [2, 3.1, 3.8, 5.1, 6]
# print(D)
# print(L)
Ws = standReges(D, L)
print(Ws)

# 绘画散点图
import matplotlib.pyplot as plt
DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.show()

# 排序后大小改变
Dcopy = DArr.copy()
# print(Dcopy[:5])
# 升序排序
Dcopy.sort(0)
# print(Dcopy[:5])

line_y = Dcopy * Ws
import matplotlib.pyplot as plt

DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.plot(Dcopy[:, 1], line_y, c='r')
plt.show()
