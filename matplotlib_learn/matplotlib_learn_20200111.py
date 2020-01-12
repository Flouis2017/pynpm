# coding:utf8
import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = "SimHei"
mpl.rcParams['axes.unicode_minus'] = False  # 负号使用默认字体

""" 柱状图(垂直)/条形图(水平) matplotlib.pyplot.bar/barh，适用场景：数据大小对比 """
# plt.bar(x=[1, 2, 3, 4], height=[10, 25, 30, 50])
# plt.barh(y=["第一季度", "第二季度", "第三季度", "第四季度"], width=[10, 25, 30, 50])
# plt.show()

""" 饼状图 matplotlib.pyplot.pie，适用场景：数据占比 """
"""
plt.pie(x=[7, 5, 3], labels=["美国", "中国", "日本"], explode=[0, 0, 0.1],
        colors=['#4169E1', '#DC143C', '#008B8B'],
        autopct="%.2f%%",  # 比例格式
        shadow=True
        )
plt.show()
"""

""" 散点图 matplotlib.pyplot.scatter，适用场景：数据分布 """
xs = np.random.randint(0, 100, 100)
ys = np.random.randint(0, 100, 100)
plt.scatter(x=xs, y=ys)
plt.show()




































