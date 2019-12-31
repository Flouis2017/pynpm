# coding: utf-8
import numpy as np

print(np.__version__)

''' numpy 最核心的类型：ndarray，本节学习numpy数组的初始化/创建 '''

# 一维数组
# a = np.array([1, 2, 3, 4])
# print(a)
# 二维数组
# b = np.array([[1, 2], [3, 4]])
# print(b)

# arange方法类似与Python原生的的range方法，不过arange的步长可以是小数，而range不可以
# c = np.arange(1, 10, 1.5)
# print(c)

# ones方法用于创建元素全部为1的数组，第一个参数(元组)指定数组形状，比如(5, 3)表示五行三列的二维数组，(5,)表示创建具有五个元素的一维数组
# d = np.ones(shape=(5,))
# print(d)
# d = np.ones(shape=(3, 3))
# print(d)
# # ones_like方法与ones方法类似，形状由已知数组决定
# d = np.ones_like(a)
# print(d)
# d = np.ones_like(b)
# print(d[0][0])

# e = np.zeros(shape=(3,))
# print(e)
# e = np.zeros(shape=(5, 5))
# print(e)
# e = np.zeros_like(a)
# print(e)
# e = np.zeros_like(b)
# print(e)

# full方法和ones方法类似，第二参数指定用什么值进行初始化
# h = np.full((3,), 6)
# print(h)
# h = np.full_like(b, 6)
# print(h)

# eye方法和identity方法可以创建一个单位矩阵——主对角线上全是1的二维数组，参数指定二维数组大小
# i = np.eye(5)
# print(i)
# i = np.identity(4)
# print(i)

# linespace方法用于创建一个等差数列，参数列表：起始、结束，长度，是否包含结束
# ls = np.linspace(10, 100, 20, endpoint=False)
# print(ls)

# 【注意】：arange方法和linspace方法很像——都能创建等差数列，区别是arange侧重于步长，linspace侧重于元素个数

# ndarray矢量运算
# 标量广播运算
# arr = np.arange(5)
# print(arr)
# print(arr+3)
# print(arr*2)

# arr2 = np.arange(10, 15)
# print(arr2)
# print(arr+arr2)

# 矢量广播运算
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
c = np.array([[10], [20]])
print(a+b)  # 纵向广播
print(b+c)  # 横向广播

