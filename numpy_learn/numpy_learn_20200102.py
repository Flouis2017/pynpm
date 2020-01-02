# coding: utf-8
import numpy as np

"""
轴（axis）：统计的方向
假设一组数据有n个维度，那么轴的取值范围是[0, n-1]的整数，0是最高维度，n-1是最低维度，
同时轴也可以取负数，负数范围是[-n, -1]，-n表示最高维度，-1表示最低维度
"""
# x = np.arange(1, 11)
# print("%s, mean: %.2f" % (x, np.mean(x)))
# x = x.reshape((2, 5))
# print("%s, mean: %.2f" % (x, np.mean(x)))
# print("维度：%s, 形状：%s, 元素类型：%s, 元素总数：%s, 元素单位：%s" % (np.ndim(x), np.shape(x), x.dtype, np.size(x), x.itemsize))
# print("高维取均：%s\n低维取均：%s" % (np.mean(x, axis=0), np.mean(x, axis=1)))
# print("高维取均：%s\n低维取均：%s" % (x.mean(axis=-2), x.mean(axis=-1)))

"""
通过多维度数组，理解轴的概念
统计规则——当ndarray扩展到多个维度（三维及以上）的统计规则：指定统计的轴下标改变，其他轴下标不变，对这些元素进行统计
"""

# x = np.arange(24).reshape((2, 3, 4))
# print("原三维数组：\n%s\n" % x)
# print("高维求和：\n%s\n" % np.sum(x, axis=0))  # x[0][0][0] + x[1][0][0], x[0][1][0] + x[1][1][0]...
# x[0][0][0] + x[0][1][0] + x[0][2][0], x[0][0][1] + x[0][1][1] + x[0][2][1]...
# print("次维求和：\n%s\n" % np.sum(x, axis=1))
# x[0][0][0] + x[0][0][1] + x[0][0][2] + x[0][0][3], x[0][1][0] + x[0][1][1] + x[0][1][2] + x[0][1][3]...
# print("低维求和：\n%s\n" % np.sum(x, axis=2))


# np.random：随机函数库
# x = np.random.rand()  # 随机产生[0, 1)之间的随机浮点数
# print("%.2f" % x)
# x = np.random.rand(2, 3)
# print(x)
# x = np.random.random((3, 3))
# print(x)
# x = np.random.randn(5, 3)  # 产生标准正太分布
# print(x)

# np.random.seed(2)  # 产生相同的随机结果
# x = np.random.randint(low=1, high=10, size=(2, 3))  # np.random.ranint()产生整数ndarray
# print(x)
# np.random.shuffle(x)  # “洗牌”
# print(x)

# x = np.random.uniform(low=1, high=10, size=(2, 3))  # np.random.uniform()产生浮点数ndarray
# print(x)

# 连接与拆分方法
# x = np.arange(1, 10).reshape((3, 3))
# print(x)
# y = np.arange(10, 19).reshape((3, 3))
# print(y)
# xy = np.concatenate((x, y), axis=0)
# print(xy)  # 按行合并
# yx = np.concatenate((x, y), axis=1)
# print(yx)  # 按列合并

# x = np.split(xy, 2, axis=0)  # 按行拆分成2部分，每部分有若干行
# print(x)
# y = np.split(yx, [2, 5], axis=1)  # 按列拆分成2部分，每部分有若干列
# print(y)

# 其他方法
x = np.array([9, 6, 2, 4, 0, 5])
y = x[::-1]  # 倒序
print(y)
x = np.reshape(x, (2, 3))
x = np.sort(x)
print(x[::-1])








