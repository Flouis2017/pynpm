# coding:utf8
import numpy as np
import pandas as pd

print("pandas version: %s\n" % pd.__version__)

# ndarray根据下标进行对位运算，而Series是根据key进行对位运算，如果对位有个key不存在则会产生NaN值
# a = np.array([1, 2, 3])
# b = np.array([10, 11, 12])
# print("a - b: %s\n" % (a - b))

# a = pd.Series([1, 2, 3], index=[1, 2, 3])
# b = pd.Series([10, 11, 12])
# print("a - b:\n%s" % (a - b))
# 如果不想产生可能出现的NaN结果，可以使用Series提供的运算方法：
# print("a - b:\n%s" % a.sub(b, fill_value=0))

# numpy提供的统计函数，sum/mean等通用也适用于Series。
# 区别是 ndarray数组与Series在计算时，对空值的处理不同。对于ndarray有一个空值则直接返回控制，
# 对于Series会忽略空值继续统计
# a = np.array([1, 2, 3, 4, np.NaN])
# s = pd.Series([1, 2, 3, 4, np.NaN])
# print("np.sum(a): %s" % np.sum(a))
# print("np.sum(s): %s" % np.sum(s))

"""
DataFrame是一个多维数组类型，因为通常使用二维数组，因此，我们可以将DataFrame理解成类似Excel的表格型数据类型。
DataFrame一行或一列都是一个Series
"""
# 初始化/创建方式：
# 方式一：pandas.DataFrame(<二维数组>)
# a = pd.DataFrame(np.random.randint(1, 20, (2, 3)))
# print("%s:\n%s" % (type(a), a))

# 方式二：通过字典来创建DataFrame —— 字典的每组键值对表示DataFrame的一个列。键值对的key用来指定列标签索引，
# 键值对的value用来指定该列的值
# df = pd.DataFrame({'A': [10, 20, 30], 'B': [2.3, 4.5, 9], 'C': ['xx', 'yy', 'zz']})
# print(df)

# DataFrame.index属性：修改行标签，DataFrame.columns属性：修改列标签
# df.index = ['2018年', '2019年', '2020年']
# print(df)
# df.columns = ['中国', '美国', '综合评价']
# print(df)

# 索引某个特定值
# print(df.values[0][1])

# 获取某一列
# col = df['中国']
# print("%s:\n%s" % (type(col), col))
# col = df.中国     # 不建议使用
# print("%s:\n%s" % (type(col), col))

# 新增一列
# df['A'] = [111, 222, 333]
# print(df)

# 删除一列
# df.pop('A')
# print(df)

# 获取某一行
# row = df.loc['2018年']
# print("%s:\n%s" % (type(row), row))
# row = df.iloc[1]
# print("%s:\n%s" % (type(row), row))

# 增加行
# df.loc['2021年'] = [0, 0, np.NaN]
# print(df)

# 删除行
# df.drop('2021年', axis=0, inplace=True)
# print(df)

df = pd.DataFrame({'苹果': [10, 20, 30], '香蕉': [2.3, 4.5, 9], '桃子': [4, 5, 6]})
print(df)
df.index = ['1月', '2月', '3月']
print(df)
# 获取DataFrame某个元素
# 先根据行再根据列
print(df.loc['1月'].loc['苹果'])
# 先根据列再根据行
print(df['香蕉'].loc['1月'])

# 获取多行多列
print(df[['苹果', '桃子']].loc[['1月', '3月']])

















