# coding:utf8
import numpy as np

xx = (0, 0, 1, 4, 3, 2, 7, 6, 5, 0)
print(type(xx))

# 一维数组
print("\n========== 1D Array begin ==========")
arr_a = np.array([0, 0, 1, 4, 3, 2, 7, 6, 5, 0])
arr_b = np.array((0, 0, 1, 4, 3, 2, 7, 6, 5, 0))
arr_c = np.arange(10)
arr_d = np.linspace(2, 10, 5)

print(arr_a)
print(arr_b)
print(arr_c[0])
print(arr_d)
print(type(arr_d[0]), arr_d[0])
print("========== 1D Array end ==========\n")

# 多维数组——注意多维数组跟矩阵是不同的概念，不能混淆
print("\n========== MD Array begin ==========")
md = np.array([
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20],
	[21, 22, 23, 24, 25],
	[26, 27, 28, 29, 30],
	[31, 32, 33, 34, 35]])
print(md)

# 多维数组切片
print(md[1][1], md[1, 1])
print(md[0, 1:4])
print(md[1:4, 2])
print(md[2, :])
print(md[:, 2])
print(md[1:4, 1:4])

# 多维数组属性
print(type(md))		# <class 'numpy.ndarray'>
print(md.dtype)		# int32
print(md.size)		# 25
print(md.shape)		# (5, 5)
print(md.ndim)		# 2
print("========== MD Array end ==========\n")

# 数组操作
print("\n========== Array Operation begin ==========")
a = np.arange(4)
# 通过reshape()转为二维数组
a = a.reshape((2, 2))
print(str(a))

b = np.array([8, 6, 2, 4])
b = b.reshape((2, 2))
print(str(b))

# 这是数组的加减乘除，不是矩阵的加减乘除！！
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

c = np.arange(10)
print("c: " + str(c))
print("c.sum(): " + str(c.sum()))
print("c.min(): " + str(c.min()))
print("c.max(): " + str(c.max()))
print("c.cumsum(): " + str(c.cumsum()))
print("========== Array Operation end ==========\n")

# 花式索引
print("\n========== Fancy indexing begin ==========")
a = np.arange(0, 20, 2)
print("a: " + str(a))

indexes = [1, 5, -2]
b = a[indexes]
print("b: " + str(b))

c = a[a >= 10]
print("c: " + str(c))
print("========== Fancy indexing end ==========\n")

