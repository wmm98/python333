import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('D:\ 广州天气.csv')
data = np.array(data)

labels = data[:, 4:5]

# 最高气温标签
labels_list = []
for i in labels:
    labels_list.append(i[0])

data_set = []
for i in data:
    data_set.append([i[2], i[3], i[5], i[6], i[7]])

x_train, x_test, y_train, y_test = train_test_split(data_set, labels_list, test_size=0.2, random_state=42)
x_trian = np.array(x_train)
y_trian = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# print(y_test)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.metrics import accuracy_score
clf = KNeighborsClassifier(1)
clf.fit(x_train, y_train)
print("*"*30)
print('KNeighborsClassifier')
print('=========结果=========')
train_predictions = clf.predict(x_test)
acc = accuracy_score(y_test, train_predictions)
print("Accuracy: {:.4%}".format(acc))
print("="*30)
