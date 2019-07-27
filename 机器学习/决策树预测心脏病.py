import csv
from numpy import mat
import random
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np

filename = 'D:\课\机器学习\机器学习作业\机器学习作业\heart.csv'
with open(filename) as f:
    reader = csv.reader(f)
    l = list(reader)[1:]
    # np.random.shuffle(l)
    labels = []
    result_data = []
    for i in l:
        data = []
        labels.append(i[-1])
        for j in i[:-1]:
            data.append(float(j))
        result_data.append(data)
#     result_data = mat(result_data)
#     print(result_data)

x_train, x_test, y_train, y_test = train_test_split(np.array(result_data), np.array(labels), test_size=0.3)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)
# print(list(y_test))

# clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=None, min_samples_split=2,
#                        min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None,
#                        max_leaf_nodes=None,
#                        min_impurity_decrease=0.0, min_impurity_split=1e-7, class_weight=None, presort=False)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
result_labels = []
result_labels = clf.predict(x_test)
clf1 = clf.score(x_test, y_test)
print("预测准确率为:")
print(clf1)
# for k in x_test:
#     result_labels.append(clf.predict(k))
# print(result_labels)

# count = 0
# for t in range(len(y_test)):
#     if y_test[t] == result_labels[t]:
#         count += 1
# print("预测准确率为%.4f" % (count / len(y_test)))
#
# # # 训练数据
# # train_data = result_data[50:261]
# # # train_data = result_data[:211]
# # train_data = mat(train_data)
# # # print(train_data[:5])
# # # print(len(train_data))
# # test_data = result_data[:50] + result_data[261:]
# # # test_data = result_data[211:]
# # test_data = mat(test_data)
# # # print(test_data[:5])
# # # print(len(test_data))
# #
# # # 训练标签
# # train_labels = labels[50:261]
# # # train_labels = labels[:211]
# # # print(train_labels[:5])
# # # print(len(train_labels))
# # test_labels = labels[:50] + labels[261:]
# # # test_labels = labels[211:]
# # # print(test_labels[:5])
# # # print(len(test_labels))
#
# # clf = tree.DecisionTreeClassifier(criterion='entropy')
# # clf = clf.fit(train_data, train_labels)
# # result_labels = []
# # for k in test_data:
# #     result_labels.append(clf.predict(k))
# # # print(result_labels)
# #
# # count = 0
# # for t in range(len(test_labels)):
# #     if test_labels[t] == result_labels[t][0]:
# #         count += 1
# # print("预测准确率为%.4f" % (count / len(test_labels)))
