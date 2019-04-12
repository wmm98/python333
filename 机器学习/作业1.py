import numpy as np
from numpy import mat
import matplotlib.pyplot as plt


def standReges(XArr, yArr):
    XMat = mat(XArr)
    yMat = mat(yArr).T
    XTX = XMat.T * XMat
    if np.linalg.det(XTX) == 0.0:
        print("This matrix is singular,cannot do inverse")
        return
    Ws = XTX.I * XMat.T * yMat
    return Ws


# 数据集
D = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
L = [2, 3.1, 3.8, 5.1, 6]
Ws = standReges(D, L)
print(Ws)

# 绘画散点图
DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.show()

# 排序后大小改变
Dcopy = DArr.copy()
# print(Dcopy[:5])
# 升序排序
# Dcopy.sort(0)
# print(Dcopy[:5])

# 直线方程
line_y = Dcopy * Ws

DArr = np.array(D)
LArr = np.array(L)
plt.scatter(DArr[:, 1], LArr)
plt.plot(Dcopy[:, 1], line_y, c='r')
plt.show()
