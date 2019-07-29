#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os

save_path = 'D:\\课\\机器学习\\树叶分类\\i_image'
if os.path.exists(save_path) is False:
    os.makedirs(save_path)

# In[2]:


img_path = 'D:\课\机器学习\树叶分类\树叶分类\leaf-classification\images'
img_name_list = os.listdir(img_path)
# print(img_name_list)
# 对文件名称重新排序
img_name_list.sort(key=lambda x: int(x.split('.')[0]))  # 按照第一个数字排序
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

# In[4]:


##顺序读取前4张图片并排序
DImage = []
for img_name in img_name_list[:4]:
    img_full_path = os.path.join(img_path, img_name)
    #     print(img_full_path)
    DImage.append(img.imread(img_full_path))
#     print(img.imread(img_full_path))


# # 图像名称对应图像ID（注意图像ID需要重新按照从小到大排序)

# In[5]:


##可视化树叶图片
f = plt.figure(figsize=(10, 10))
for i in range(4):
    plt.subplot(3, 4, i + 1)
    plt.axis("off")
    plt.title("image_ID:{0}".format(img_name_list[i].split('.jpg')[0]))
    #     print("image_ID:{0}".format(img_name_list[i].split('.jpg')))
    plt.imshow(DImage[i], cmap='hot')
plt.show()

# In[6]:


import pandas as pd

train = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\train.csv')
Train_id = train['id']
Test = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\test.csv')
Test_id = Test['id']
Test.drop(['id'], inplace=True, axis=1)

# In[7]:


train.head()

# In[8]:


Test.head()

# In[9]:


# train['species'].value_counts()
print("树叶种类数目为：", len(set(train['species'])))

# In[10]:


## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic = {};
i = -1
for _ in train['species']:
    if _ in map_dic:
        pass
    else:
        i += 1
        map_dic[_] = map_dic.get(_, i)

# In[11]:


train['Type'] = train['species'].map(map_dic)
# print(train['Type'])
train.drop(['species'], inplace=True, axis=1)
train.drop(['id'], inplace=True, axis=1)

# In[13]:


train.head()

# # 画出相关性矩阵（需要根据相关性矩阵，选择特征进行特征工程）

# In[14]:


import seaborn as sns
import matplotlib.pyplot as plt

# 相关系数矩阵
corr = train.corr()
# print(corr)
f, ax = plt.subplots(figsize=(25, 25))
# 为离散的数据创建一个定制的颜色映射
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5)
plt.show()

# In[15]:


for _ in train.isna().sum():
    if _ != 0:
        print('存在缺失值')

# In[16]:


X = train.drop(['Type'], axis=1)
y = train['Type']
print(y.head())
print("训练集尺寸:", X.shape)

# In[17]:


##原始数据
## 划分训练集和测试集
from sklearn.model_selection import train_test_split

X1_train, X1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("训练集数据尺寸", X1_train.shape)
print("测试集数据尺寸", X1_test.shape)
print("训练集目标尺寸", y1_train.shape)
print("测试集目标尺寸", y1_test.shape)

# # 数据特征一共有192个，可用PCA 变换对数据降维
# 

# In[18]:


train = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\train.csv')
# 把trani.csv文件的数据的第一、二列去掉
train_data = train.iloc[:, 2:]
# 将数据转成数组形式
train_data = np.array(train_data)
train_data

# In[19]:


from sklearn.decomposition import PCA

# n_components表示PCA算法中所要保留的主成分个数n，也即保留下来的特征个数n
pca = PCA(n_components=192)
# fit(train_data)，表示用数据train_data来训练PCA模型
pca.fit(train_data)
# 用train_data来训练PCA模型，同时返回降维后的数据，newData就是降维后的数据
result = np.array(pca.explained_variance_ratio_)

# # 每个特征值所占的比列

# In[20]:


result

# # 通过简单的计算计出所要降到的维数

# In[21]:


result = np.array(pca.explained_variance_ratio_)
print(result)
count = 0

for i in range(0, len(result)):
    if count >= 0.95:
        print('维数：' + str(i))
        break
    else:
        count += result[i]

print(count)

# # PCA降到48维

# In[22]:


from sklearn.decomposition import PCA

# n_components表示PCA算法中所要保留的主成分个数n，也即保留下来的特征个数n
pca = PCA(n_components=48)
# fit(train_data)，表示用数据train_data来训练PCA模型
pca.fit(train_data)
# 用train_data来训练PCA模型，同时返回降维后的数据，newData就是降维后的数据
newData = pca.fit_transform(train_data)

# # 降维后的数据

# In[23]:


newData

# # 打印主成分总和超过95%的前18个特征的贡献率

# In[24]:


for jj in range(len(result[:48])):
    print('第' + str(jj) + '个成分可以解析' + str(result[jj] * 100) + '%' + '的数据')

# # 对PCA变换后的数据做归一化处理，将数据归一化到【0，1】

# In[25]:


## 此处完成PCA coding
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
x_minmax = min_max_scaler.fit_transform(newData)

# # 降维并归一化之后的数据

# In[26]:


x_minmax

# # 划分数据

# In[27]:


## 划分训练集和测试集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_minmax, y, test_size=0.2, random_state=42)
print("训练集数据尺寸", X_train.shape)
print("测试集数据尺寸", X_test.shape)
print("训练集目标尺寸", y_train.shape)
print("测试集目标尺寸", y_test.shape)

# # 使用机器学习算法（下面是分类的算法）
# 

# # X_train, X_test, y_train, y_test >>> 是降维跟归一化之后的数据）（X1_train, X1_test, y1_train, y1_test >>> 是降维跟归一化之前的数据）可以两种数据都测试分类算法查看准确率

# In[28]:


# 降维和归一化之后的数据，除了随机森林算法，其他准确率略有提升
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC  # SVC：支持向量机  LinearSVC：线性分类支持向量机  NuSVC：
from sklearn.tree import DecisionTreeClassifier  # 决策树分类器
from sklearn.ensemble import RandomForestClassifier  # 随机森林
from sklearn.naive_bayes import GaussianNB  # 高斯贝叶斯分类器
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis  # 线性判别分析
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis  # 二次判别分析

classifiers = [
    KNeighborsClassifier(3),
    # C越大，即对分错样本的惩罚程度越大，因此在训练样本中准确率越高，但是泛化能力降低，也就是对测试数据的分类准确率降低。
    # 第二个参数：'ovo’, ‘ovr’ or None
    # 第三个参数：‘如果gamma为auto，代表其值为样本特征数的倒数
    SVC(C=10, decision_function_shape='ovr', gamma='scale'),
    NuSVC(probability=True),
    GaussianNB(),
    LinearDiscriminantAnalysis(),
    RandomForestClassifier()]

for clf in classifiers:
    clf.fit(X_train, y_train)
    name = clf.__class__.__name__

    print("=" * 30)
    print(name)

    print('****Results****')
    train_predictions = clf.predict(X_test)
    acc = accuracy_score(y_test, train_predictions)
    print("Accuracy: {:.4%}".format(acc))

print("=" * 30)

# # 原始数据进行训练预测

# In[29]:


# 原始数据进行训练
for clf in classifiers:
    clf.fit(X1_train, y1_train)
    name = clf.__class__.__name__

    print("=" * 30)
    print(name)

    print('****Results****')
    train_predictions = clf.predict(X1_test)
    acc = accuracy_score(y1_test, train_predictions)
    print("Accuracy: {:.4%}".format(acc))

print("=" * 30)

# # 对测试集的树叶图片进行分类

# In[30]:


from sklearn.svm import SVC, LinearSVC, NuSVC

# 使用svc进行分类
# rf_test = LinearDiscriminantAnalysis()
rf_test = SVC(C=10, decision_function_shape='ovr', gamma='scale')
rf_test = RandomForestClassifier()
rf_test.fit(X1_train, y1_train)
res = rf_test.predict(Test)
print("预测结果尺寸为:", res.shape)

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(res == i)[0].tolist()
#     print(np.where(res==i)[0].tolist())

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(y.values == i)[0].tolist()

# In[31]:


DImage = []  ###建立所有图片的数据集
for img_name in img_name_list:
    img_full_path = os.path.join(img_path, img_name)
    DImage.append(img.imread(img_full_path))

# In[32]:


img_full_path


# # 图片分类函数实现

# In[33]:


def imagesclassifier(DImage, Train_id, Test_id, Train_label_dic, Test_label_dic, root_path):
    '''DImage为图像数据集(循环读取的1584张图片)，Train_id,Test_id分别是train.csv
    和test.csv 内id列，Train_label_dic,Test_label_dic是树叶类别标签和图片索引对应关系'''
    if os.path.exists(root_path) is False:
        os.makedirs(root_path)
    save_path = root_path
    for i in range(99):
        j = 0
        train_val = Train_id.values[np.array(Train_label_dic[i])] - 1
        #         print(train_val)
        test_val = Test_id.values[np.array(Test_label_dic[i])] - 1
        Train_imgs = np.array(DImage)[train_val]
        #         print(Train_imgs)
        Test_imgs = np.array(DImage)[test_val]
        for index, _ in enumerate(Train_imgs):
            #             print(index, _)
            img_name = 'train' + str(train_val[index]) + '.jpg'
            save_path = os.path.join(save_path, str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path, img_name), _, cmap='binary')
            save_path = root_path
            j += 1

        for index, _ in enumerate(Test_imgs):
            img_name = 'test' + str(test_val[index]) + '.jpg'
            save_path = os.path.join(save_path, str(i))
            if os.path.exists(save_path) is False:
                os.makedirs(save_path)
            img.imsave(os.path.join(save_path, img_name), _, cmap='binary')
            save_path = root_path
            j += 1


# In[34]:


imagesclassifier(DImage, Train_id, Test_id, Train_label_dic, Test_label_dic, save_path)

# # 利用聚类进行图片分类

# # 简单处理数据

# In[35]:


import pandas as pd

train_test = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\train.csv')
TrainNew_id = train_test['id']
Test_test = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\test.csv')
TestNew_id = Test_test['id']

train = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\train.csv', index_col='id')
Test = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\test.csv', index_col='id')

# In[36]:


train.drop(['species'], inplace=True, axis=1)
train_data = train.iloc[:, :]
test_data = Test.iloc[:, :]

# # 合并训练数据和测试数据

# In[37]:


frames = [train, Test]
result = pd.concat(frames)

# # 数据标准化

# In[38]:


# 数据标准化  #z-score标准化法 z-score 标准化(zero-mean normalization)也叫标准差标准化，经过处理的数据符合标准正态分布，即均值为0，标准差为1
data2 = 1.0 * (result - result.mean()) / result.std()
data1 = data2[data2.columns[:]].as_matrix()

# # 调用k-means

# In[39]:


from sklearn.cluster import KMeans

model = KMeans(n_clusters=99, n_jobs=4)  # 分为k类，并发数4
model.fit(data1)  # 开始聚类

# 简单打印结果
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(result.columns) + [u'类别数目']

# In[40]:


r = pd.concat([result, pd.Series(model.labels_, index=result.index)], axis=1)  # 详细输出每个样本对应的类别

r.columns = list(result.columns) + [u'species']  # 重命名表头

# In[41]:


r.head()

# In[42]:


species = list(r['species'])

# In[43]:


train_spe, test_spe = np.array(species[:990]), np.array(species[990:])

# # 分图片

# In[44]:


import numpy as np

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(test_spe == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(train_spe == i)[0].tolist()

# In[45]:


imagesclassifier(DImage, TrainNew_id, TestNew_id, Train_label_dic, Test_label_dic, save_path)

# # DBSCAN参数调整

# In[46]:


from sklearn.cluster import DBSCAN
import pandas as pd
import numpy as np

# 构建空列表，用于保存不同参数组合下的结果
res = []
# 迭代不同的eps值
for eps in np.arange(6, 6.05, 0.001):
    # 迭代不同的min_samples值
    for min_samples in range(12, 15):
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        # 模型拟合
        dbscan.fit(data1)
        # 统计各参数组合下的聚类个数（-1表示异常点）
        n_clusters = len([i for i in set(dbscan.labels_) if i != -1])
        # 异常点的个数
        outliners = np.sum(np.where(dbscan.labels_ == -1, 1, 0))
        # 统计每个簇的样本个数
        stats = str(pd.Series([i for i in dbscan.labels_ if i != -1]).value_counts().values)
        res.append(
            {'eps': eps, 'min_samples': min_samples, 'n_clusters': n_clusters, 'outliners': outliners, 'stats': stats})
# 将迭代后的结果存储到数据框中
df = pd.DataFrame(res)

# 根据条件筛选合理的参数组合
df.loc[df.n_clusters == 3, :]
print(df)

# # DBSCAN密度聚类算法

# In[47]:


from sklearn.cluster import DBSCAN

# 设置半径为10，最小样本量为2，建模
db = DBSCAN(eps=6.449, min_samples=2).fit(data1)

r = pd.concat([result, pd.Series(db.labels_, index=result.index)], axis=1)  # 详细输出每个样本对应的类别

r.columns = list(result.columns) + [u'species']  # 重命名表头
# 注：cluster列是kmeans聚成3类的结果；cluster2列是kmeans聚类成2类的结果；scaled_cluster列是kmeans聚类成3类的结果（经过了数据标准化）


# In[48]:


r.head()

# # Birch聚类（层次聚类）

# In[49]:


from sklearn.cluster import Birch

# 如果类别数非常多，我们也没有先验知识，则一般输入None，默认是3
model = Birch(n_clusters=99)
model.fit(data1)
r = pd.concat([result, pd.Series(model.labels_, index=result.index)], axis=1)  # 详细输出每个样本对应的类别

r.columns = list(result.columns) + [u'species']  # 重命名表头

# In[50]:


r.head()

# In[51]:


species = list(r['species'])
train_spe, test_spe = np.array(species[:990]), np.array(species[990:])

# In[52]:


import numpy as np

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(test_spe == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(train_spe == i)[0].tolist()

# In[53]:


imagesclassifier(DImage, TrainNew_id, TestNew_id, Train_label_dic, Test_label_dic, save_path)

# # Mini Batch K-Means聚类（Mini Batch K-Means是K-Means算法的一种优化方案，主要优化了数据量大情况下的计算速度）

# In[54]:


# Mini Batch K-Means中多了一个方法，partial_fit，即可以只用一个batch_size进行训练。其他与K-Means相同。

from sklearn.cluster import MiniBatchKMeans

model = MiniBatchKMeans(n_clusters=99)
model.fit(data1)

# In[55]:


r = pd.concat([result, pd.Series(model.labels_, index=result.index)], axis=1)  # 详细输出每个样本对应的类别

r.columns = list(result.columns) + [u'species']  # 重命名表头

# In[56]:


r.head()

# In[57]:


species = list(r['species'])
train_spe, test_spe = np.array(species[:990]), np.array(species[990:])

# In[58]:


import numpy as np

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(test_spe == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(train_spe == i)[0].tolist()

# In[59]:


imagesclassifier(DImage, TrainNew_id, TestNew_id, Train_label_dic, Test_label_dic, save_path)

# # AgglomerativeClustering聚类（层次聚类）

# In[60]:


from sklearn.cluster import AgglomerativeClustering

# n_clusters：一个整数，指定分类簇的数量
# affinity：一个字符串或者可调用对象，用于计算距离。
# 可以为：’euclidean’，’l1’，’l2’，’mantattan’，’cosine’，’precomputed’，如果linkage=’ward’，则affinity必须为’euclidean’
# 如果compute_full_tree=True，则会继续训练从而生成一颗完整的树
model = AgglomerativeClustering(affinity='euclidean', n_clusters=99, compute_full_tree=True)
model.fit(data1)

# In[61]:


r = pd.concat([result, pd.Series(model.labels_, index=result.index)], axis=1)  # 详细输出每个样本对应的类别

r.columns = list(result.columns) + [u'species']  # 重命名表头

# In[62]:


species = list(r['species'])
train_spe, test_spe = np.array(species[:990]), np.array(species[990:])

# In[63]:


import numpy as np

Test_label_dic = {}
for i in range(99):
    Test_label_dic[i] = np.where(test_spe == i)[0].tolist()

Train_label_dic = {}
for i in range(99):
    Train_label_dic[i] = np.where(train_spe == i)[0].tolist()

# In[64]:


imagesclassifier(DImage, TrainNew_id, TestNew_id, Train_label_dic, Test_label_dic, save_path)

# # 网格搜索进行调参

# In[73]:


from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
import numpy as np
import pandas as pd

train = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\train.csv')
Test = pd.read_csv('D:\\课\\机器学习\\树叶分类\\树叶分类\\leaf-classification\\test.csv')

# In[2]:


# train.head()


# In[3]:


# Test.head()


# In[74]:


train_data = train.iloc[:, 2:]
# print(train_data)
train_data = np.array(train_data)
# print(train_data)
# print(len(train_data))
## 把species转换为类标签。如把树叶名Acer_Opalus转为0
map_dic = {};
i = -1
for _ in train['species']:
    if _ in map_dic:
        pass
    else:
        i += 1
        map_dic[_] = map_dic.get(_, i)

train['Type'] = train['species'].map(map_dic)
# train.head()

train_label = np.array(train.iloc[:, -1])
# print(train_label)


# In[75]:


from sklearn.model_selection import train_test_split

# # 划分数据集train_test_split() 第一个参数表示特征值，第二个参数表示目标值，test_size表示测试集所占的百分比(推荐0.25)
x_train, x_test, y_train, y_test = train_test_split(train_data, train_label, test_size=0.2)  # 划分是按比例随机划分
# 返回值 x_train表示训练集的特征值，x_test表示测试集的特征值，y_train表示训练集的目标值，y_test表示测试集的目标值


# # 证明划分数据训练集准确率达到0.8以上

# In[148]:


from sklearn.ensemble import ExtraTreesClassifier

ExtraTreesClassifier = ExtraTreesClassifier()
ExtraTreesClassifier.fit(x_train, y_train)
ExtraTreesClassifier.score(x_train, y_train)

# In[149]:


ExtraTreesClassifier.score(x_test, y_test)


# In[ ]:


# In[133]:


def pca(D, numfeat):
    DMat = np.array(D)
    mean_removed = DMat - DMat.mean(axis=0)
    DCovMat = np.cov(mean_removed, rowvar=0)
    eigval, eigvec = np.linalg.eig(DCovMat)
    ###选择特征值前numfeat大的特征向量索引
    tar_index = np.argsort(eigval)[:-(numfeat + 1):-1]
    ##选取的特征向量
    reduced_vec = eigvec[:, tar_index]
    lowDataSet = np.dot(mean_removed, reduced_vec)
    reconstructMat = np.dot(lowDataSet,
                            reduced_vec.T) + DMat.mean(axis=0)
    # print(reconstructMat.shape)
    return lowDataSet, reconstructMat


# In[78]:


lowDataSet, reconstructMat = pca(train_data, 48)

# In[79]:


X_train, X_test, Y_train, Y_test = train_test_split(lowDataSet, train_label, test_size=0.2)  # 划分是按比例随机划分

# # Grid Search：一种调优方法，在参数列表中进行穷举搜索，对每种情况进行训练，找到最优的参数

# # # 网格搜索调参

# In[ ]:


# 4，max_depth: (default=None)设置树的最大深度，默认为None，这样建树时，会使每一个叶节点只有一个类别，或是达到min_samples_split。
# 5，min_samples_split:根据属性划分节点时，每个划分最少的样本数。
# 6，min_samples_leaf:叶子节点最少的样本数。
# 7，max_leaf_nodes: (default=None)叶子树的最大样本数。
# 8，min_weight_fraction_leaf: (default=0) 叶子节点所需要的最小权值
# 9，verbose:(default=0) 是否显示任务进程
# n_estimators=10：决策树的个数，越多越好，但是性能就会越差，至少100左右可以达到可接受的性能和误差率。 
param_test1 = {'n_estimators': [50, 120, 160, 200, 250]}
gsearch1 = GridSearchCV(estimator=RandomForestClassifier(min_samples_split=100,
                                                         min_samples_leaf=20, max_depth=8, max_features='sqrt',
                                                         random_state=10),
                        param_grid=param_test1, scoring='roc_auc', cv=5)
gsearch1.fit(x_train, y_train)
print(gsearch1.best_params_, gsearch1.best_score_)  # ,gsearch1.cv_results_打印拟合结果)

# In[30]:


##随机森林
##原始数据
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

n_estimators = [90, 95, 100, 105, 110]
max_depth = range(1, 30)
cv = StratifiedShuffleSplit(n_splits=10, test_size=.20, random_state=15)

parameters = {'n_estimators': n_estimators,
              'max_depth': max_depth,
              }
grid = GridSearchCV(RandomForestClassifier(),
                    param_grid=parameters,
                    cv=cv,
                    n_jobs=-1)

# In[31]:


grid.fit(x_train, y_train)
rf_grid = grid.best_estimator_

# In[32]:


rf_grid.score(x_train, y_train)

# In[33]:


rf_grid.score(x_test, y_test)

#
# #降维后

# In[34]:


grid.fit(X_train, Y_train)

# In[37]:


rf_grid = grid.best_estimator_
rf_grid.score(X_train, Y_train)

# In[38]:


rf_grid.score(X_test, Y_test)

# # SVM

# In[39]:


##原始数据
from sklearn import svm
from sklearn.model_selection import GridSearchCV
# parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
# cv = StratifiedShuffleSplit(n_splits=10, test_size=.30, random_state=15)
# svc = svm.SVC(gamma="scale")
# grid = GridSearchCV(svc, parameters, cv=cv)

# C: 目标函数的惩罚系数C，用来平衡分类间隔margin和错分样本的，default C = 1.0
# gamma：核函数的系数('Poly', 'RBF' and 'Sigmoid'), 默认是gamma = 1 / n_features;
from sklearn.svm import SVC

Cs = [0.001, 0.01, 0.1, 1, 1.5, 2, 2.5, 3, 4, 5, 10]  ## penalty parameter C for the error term.
gammas = [0.0001, 0.001, 0.01, 0.1, 1]
param_grid = {'C': Cs, 'gamma': gammas}
cv = StratifiedShuffleSplit(n_splits=10, test_size=.2, random_state=15)
grid = GridSearchCV(SVC(kernel='rbf', probability=True), param_grid, cv=cv)  ## 'rbf' stands for gaussian kernel

# In[40]:


grid.fit(x_train, y_train)  ##降维之前
# rf_grid = grid.best_estimator_
# print(rf_grid.score(x_train,y_train))
# print(rf_grid.score(x_test,y_test))


# In[41]:


rf_grid = grid.best_estimator_
print(rf_grid.score(x_train, y_train))

# In[42]:


print(rf_grid.score(x_test, y_test))

# In[43]:


####降维后
grid.fit(X_train, Y_train)

# In[44]:


rf_grid = grid.best_estimator_
print(rf_grid.score(X_train, Y_train))
print(rf_grid.score(X_test, Y_test))

# In[ ]:


# In[93]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# from sklearn.grid_search import GridSearchCV
# iris = datasets.load_iris()
param_grid = {"base_estimator__criterion": ["gini", "entropy"],
              "base_estimator__splitter": ["best", "random"],
              "n_estimators": [1, 2]}
dtc = DecisionTreeClassifier()
ada = AdaBoostClassifier(base_estimator=dtc)
# X, y = datasets.make_hastie_10_2(n_samples=12000, random_state=1)
grid = GridSearchCV(ada, param_grid=param_grid, cv=10)
# grid_search_ada.fit(x_train,y_train)


# In[94]:


grid.fit(x_train, y_train)  ##降维之前

# In[95]:


rf_grid = grid.best_estimator_

# In[96]:


print(rf_grid.score(x_train, y_train))
# print(rf_grid.score(x_test,y_test))           


# In[97]:


print(rf_grid.score(x_test, y_test))

# In[102]:


grid.fit(X_train, Y_train)  ####降维后

# In[103]:


rf_grid = grid.best_estimator_

# In[104]:


print(rf_grid.score(X_train, Y_train))

# In[105]:


print(rf_grid.score(X_test, Y_test))

# In[57]:


# max_ depth 
# 定义了树的最大深度。
# 它也可以控制过度拟合，因为分类树越深就越可能过度拟合。
# 当然也应该用CV值检验。

# min_ samples_split 
# 定义了树中一个节点所需要用来分裂的最少样本数。
# 可以避免过度拟合(over-fitting)。如果用于分类的样本数太小，模型可能只适用于用来训练的样本的分类，而用较多的样本数则可以避免这个问题。
# 但是如果设定的值过大，就可能出现欠拟合现象(under-fitting)。因此我们可以用CV值（离散系数）考量调节效果。

# n_ estimators 
# 定义了需要使用到的决定树的数量


# random_ state 
# 作为每次产生随机数的随机种子
# 使用随机种子对于调参过程是很重要的，因为如果我们每次都用不同的随机种子，即使参数值没变每次出来的结果也会不同，这样不利于比较不同模型的结果。
# 任一个随即样本都有可能导致过度拟合，可以用不同的随机样本建模来减少过度拟合的可能，但这样计算上也会昂贵很多，因而我们很少这样用


from sklearn.ensemble import GradientBoostingClassifier

param_test2 = {'max_depth': range(3, 14, 2), 'min_samples_split': range(100, 801, 200)}
gsearch2 = GridSearchCV(estimator=GradientBoostingClassifier(learning_rate=0.1, n_estimators=60, min_samples_leaf=20,
                                                             max_features='sqrt', subsample=0.8, random_state=10),
                        param_grid=param_test2, cv=5)
gsearch2.fit(x_train, y_train)  ##降维之前

# In[59]:


rf2 = gsearch2.best_estimator_

# In[60]:


print(rf2.score(x_train, y_train))

# In[61]:


print(rf2.score(x_test, y_test))

# In[62]:


gsearch2.fit(X_train, Y_train)  ##降维之后

# In[68]:


rf3 = gsearch2.best_estimator_

# In[71]:


print(rf3.score(X_train, Y_train))
print(rf3.score(X_test, Y_test))
