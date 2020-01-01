# coding: utf-8
import numpy as np

print(np.__version__)

''' 本节学习 ndarray 相关属性与操作 '''

# ndarray.ndim 属性：返回维度，1就表示一维数组，2就表示二维数组
a = np.array([1, 2, 3])
print(a.ndim)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)

# ndarray.shape 属性：返回数组有几行有几列
print(a.shape)  # (2, 3)表示二行三列
a = np.array([[1, 2], [3, 4, 5]])
print(a.shape)  # (2,)表示二行，因为列不固定，所以列的数量没有显示

a = np.array([[1, 2, 3], [4., 5, 6]])
# ndarray.dtype 属性：返回数组元素类型
print(a.dtype)
# ndarray.size 属性：返回数组元素总个数
print(a.size)
# ndarray.itemsize 属性：返回一个数组元素占用几个字节(1Byte 字节 = 8Bit 二进制/位)
print(a.itemsize)

# ndarray.reshape()方法改变数组形状
b = np.arange(24)
print(type(b))
b = np.reshape(b, (3, 8))  # 表示转化成一个三行八列的二维数组
print(b)
b = b.reshape((4, 6))
print(b)
b = b.reshape((2, -1))  # -1表示自动计算长度
print(b)

# 索引与切片: “先行后列”
c = np.arange(12)
c = c.reshape((3, 4))
print(c)
print("c[1][2]: %s" % c[1][2])
print("c[1, 2]: %s" % c[1, 2])

d = np.arange(30).reshape((5, 6))
print(d)
print("d[1:4, 1:4] :\n %s" % d[1:4, 1:4])

# 【注意】：Python列表进行切片可以用于深拷贝，但是ndarray切片返回的是原数组对象的视图，无法用于深拷贝，例子如下：
li = [1, 2, 3, 4, 5]
li2 = li[:]
li2[0] = 100
print(li)  # [1, 2, 3, 4, 5]
print(li2)  # [100, 2, 3, 4, 5]

li = np.array([1, 2, 3, 4, 5])
li2 = li[:]
li2[0] = 100
print(li)  # [100   2   3   4   5]
print(li2)  # [100   2   3   4   5]

# ndarray实现深拷贝使用copy()方法
li = np.array([1, 2, 3, 4, 5])
li2 = li.copy()
li2[0] = 100
print(li)  # [1 2 3 4 5]
print(li2)  # [100   2   3   4   5]

# 通过数组进行切片：ndarray特有，通过数组进行切片可用于深拷贝
e = np.array([1, 3, 5, 10, 9, 2])
print("e: %s" % e)
ee = e[[1, 2, 4]]
print("e[[1, 2, 4]]: %s" % ee)
ee[0] = 100
print("e / ee : %s / %s" % (e, ee))

# ravel()方法和flatten()方法都是将ndarray转成一维数组——该过程称为“扁平化”，区别在于flatten可用于深拷贝，而ravel不行
f = np.arange(10).reshape(2, 5)
print("f:%s" % f)
f = f.ravel()
print(f)
f = f.flatten()
print(f)

# 【说明】：存储顺序C/F，C代表C语言，F代表Fortune语言，C按照行优先进行存储，F按照列优先存储
# 构建数组时，会首先根据存储顺序进行扁平化，然后根据存储顺序进行填充
x = np.array([[0, 1], [2, 3]], order='C')
print("x:%s" % x)
y = np.array([[0, 1], [2, 3]], order='F')
print("y:%s" % y)

x = np.arange(4).reshape((2, 2), order='C')
print("x:%s" % x)
y = np.arange(4).reshape((2, 2), order='F')
print("y:%s" % y)

# Numpy提供了许多通用函数，这些通用函数相当于Python通用函数的矢量版 —— 消除循环
x = np.array([-1, -2.3, 3.6, 5, -9])
print(np.abs(x))    # np.abs(ndarray) 取绝对值
print(np.modf(x))   # np.modf(ndarray) 返回数组小数部分元组和整数部分元组

print('%.1f' % x.sum())
print('%.2f' % x.mean())     # ndarray.mean()求平均值
print("max: %s, min: %s" % (x.max(), x.min()))
print("max_index: %s, min_index: %s" % (x.argmax(), x.argmin()))    # 返回最大值/最小值所在的索引下标
print("标准差: %.2f, 方差: %.2f" % (x.std(), x.var()))
print("累计和: %s, 累计积: %s" % (x.cumsum(), x.cumprod()))
