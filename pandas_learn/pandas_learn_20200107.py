# coding:utf8
import numpy as np
import pandas as pd
import sqlite3

print("pandas version: %s" % pd.__version__)

# 数据加载
# 读取csv文件
# 读取文件跟文件扩展名没有关系，read_csv不是指读取csv后缀的文件，而是读取csv格式数据的文件
# 文件扩展名最主要的用途是关联打开方式，跟文件中存放的数据没有任何关系，不要混淆了！
# res = pd.read_csv("../resource/spider.csv")
# print("%s\n%s" % (type(res), res))
# print(res.head(10))

# read_csv()常用参数说明：
# filepath_or_buffer：文件路径
# header：默认情况下，将首行数据作为标题行，如果没有标题行，则设置header为None
# sep/delimiter：指定分隔符，默认使用“,”进行分割，read_table()和read_csv()十分接近，区别就是read_table方法使用\t(制表符)作为分隔符，read_csv使用逗号
# names：指定列名
# index_col：指定索引列
# usecols：指定需要读取的列，默认读取全部
"""
res = pd.read_csv(filepath_or_buffer="../resource/spider.csv", header=None,
			names=['date', 'url', 'info', 'num1', 'num2'],
			# index_col='date',
			usecols=['date', 'url', 'num1'])
# print("%s\n%s" % (type(res), res))
print(res.sample(10))  # 随机10条数据
"""

# read_sql() 从数据库中读取数据
# 首先获取连接 —— 这里为了演示的方便使用Python内嵌的sqlLite3数据库

# sqlite3.connect()参数指定连接数据库，如果不存在则创建后再进行连接
"""
con = sqlite3.connect("test.db")
# con.execute("create table person(id varchar(32) primary key, name varchar(100))")
# con.execute("insert into person values ('10001', 'Tom')")
# con.execute("insert into person values ('10002', 'Smith')")
# con.execute("insert into person values ('10003', 'Christina')")
# con.commit()

# read_sql()常用参数
# sql：查询sql
# con：数据源连接
# index_col：指定索引列
res = pd.read_sql(sql="select * from person", con=con, index_col='id')
print(res)
"""


# 数据写入
# to_csv()常用参数：
# sep：指定分隔符，默认使用,
# header：是否写入标题行，默认为True。这个参数跟之前read_csv()中的header类型不同，这里是bool类型，read_csv是一个整数类型
# na_rep：空值占位，默认都不显示。【注意】：np.NaN是浮点型——特殊的float：print(type(np.NaN))
# index：是否写入索引列，默认为True
# columns：指定写入的列
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [9, np.NaN, 0]])
df.to_csv("../resource/demo.csv", sep=",", header=False, na_rep="空值", index=False, columns=[0, 2])
# df.to_csv("../resource/demo.csv", index_label='i')





































