# coding:utf8

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("FullData.csv")
# 当列较多的时候，列不会全部显示，默认使用...进行折叠显示
pd.set_option('display.max_columns', 100)  # 设置超过100列再使用...进行折叠显示
pd.set_option('display.width', None)  # 不换行显示

# print(data.head(3))  # 打印前三条记录


# print(data.info())  # info()主要是为了查看缺失数据
# print(data[data['Club_Position'].isnull()])  # 查看缺失数据所在行的所有数据

data = data[data['Club_Position'].notnull()]  # 过滤缺失数据
# print(data.info())

# print(data.describe())  # describe()主要是为了查看异常数据
# print(data.duplicated().any())  # 查看是否有重复行
data.drop_duplicates(inplace=True)  # 过滤重复的行

# 将数值类型的字段处理为int或float，便于之后的数据分析
# print(data.sample())  # 随机取出一条数据
data['Height'] = data['Height'].apply(lambda x: x.replace("cm", "")).astype(np.int32)
data['Weight'] = data['Weight'].apply(lambda x: x.replace("kg", "")).astype(np.int32)
# print(data.sample())
# print(data.info())

# print(data[['Height', 'Weight', 'Rating']])

"""
# 运动员身高、体重、评分分布图：
ax = data[['Height', 'Weight', 'Rating']].plot(kind='kde')  # pandas也自带了画图组件
fig = ax.get_figure()
fig.savefig("normal_distribution.png")
"""

"""
# 运动员左右脚 偏差统计
# 通过groupby()方法进行分组统计
# g = data.groupby('Preffered_Foot')
# ax = g['Preffered_Foot'].count().plot(kind='bar')
# ax = g.size().plot(kind='bar')
# 或者通过通过value_counts()统计不同数据的个数，跟sql中的distinct类似，需要注意的是value_counts()默认是按降序，可以通过ascending="True"设置为升序
ax = data['Preffered_Foot'].value_counts(ascending=True).plot(kind='bar')
fig = ax.get_figure()
fig.savefig("LR_Foot.png")
"""

"""
# 根据球员平均评分，统计大于等于20人的前10名俱乐部/国家
g = data.groupby('Club')
# g = data.groupby('Nationality')
v = g['Rating'].agg(['mean', 'count'])  # agg() 按照什么维度进行统计
v = v[v['count'] >= 20].sort_values('mean', ascending=False).head(10)
print(v)
ax = v.plot(kind='bar')
plt.legend(labels=['评分', '人数'])
plt.show()
"""

"""
# 统计拥有忠心（五年及以上）球员的前十个俱乐部
year = data['Club_Joining'].apply(lambda x: x.split('/')[-1]).astype(np.int)
# print(year)
# 用获取数据集年份 和 年份数据 做差，筛选出五年以上且不是“自由身”的球员
g = data[(2017 - year >= 5) & (data['Club'] != 'Free Agents')]
# 根据俱乐部进行分组合计
g = g.groupby('Club').size().sort_values(ascending=False).head(10)
print(g)
p = g.plot(kind='bar')
plt.show()
"""
































































