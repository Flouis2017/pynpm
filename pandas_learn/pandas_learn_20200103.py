# coding:utf8
import numpy as np
import pandas as pd

print("pandas version: %s\n" % pd.__version__)

"""Series类似于Numpy中的一维数组对象，可以将该类型看作是一组数据与数据相关的标签（索引）混合构成，可以看成存放字典的一维数组"""
# Series对象初始化：pandas.Series(<可迭代对象>)
# 只要传入一个可迭代对象就可以创建一个Series对象，可以通过Python自带的list、numpy的ndarray（一维）、range()等来创建
# a = pd.Series([1, 2.2, 3])
# print("%s: \n%s" % (type(a), a))

# a = pd.Series(np.arange(7))
# print("%s: \n%s" % (type(a), a))

# a = pd.Series(range(1, 10, 2))
# print("%s: \n%s" % (type(a), a))

# a = np.array([{'name': 'Flouis'}, 23])
# print(a[0]['name'])

# 指定标签初始化——如果只有一个标量，会进行广播初始化：a = pd.Series(100, index=['abc', 'def', 'qwer'])
a = pd.Series([100, 101, 102], index=['abc', 'def', 'qwer'])
# print("%s: \n%s" % (type(a), a))

# Series的index属性：Series可以通过下标进行索引也可以通过标签，即键值对的键进行索引，所以这里的index既可以是下标也可以是键
# Series本质上是对一维的ndarray的封装，简化一维ndarray的操作
a.index = ['tom', 'micheal', 'marry']  # 通过index属性可以修改键
print("------------------------------\n%s\n------------------------------" % a)
# print("a['tom']: %s" % a['tom'])
print("a[-2]: %s" % a[-2])
# a['tom'] = 'xyz'
# print("------------------------------\n%s\n------------------------------" % a)
# index = pd.Index(['a', 'b', 'c'])
# a.index = index
# print("------------------------------\n%s\n------------------------------" % a)

# Series的values属性：返回数据列表(ndarray)
# vals = a.values
# print("%s: %s" % (type(vals), vals))

# Series的size属性：返回数据总个数
# print("size: %s, shape: %s" % (a.size, a.shape))

# Series的name属性和Series.index的name属性，是两个不同的概念
# a.name = 'my_series'
# a.index.name = 'my_index'
# print("------------------------------\n%s\n------------------------------" % a)

# Series.head(n)/Series.tail(n)，访问前/后n条记录，如果总条数小于n，则返回所有数据
# print("a.head(5): %s" % a.head(2))
# print("a.tail(6): %s" % a.tail(6))




















































