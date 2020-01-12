# coding:utf8
import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = "SimHei"
mpl.rcParams['axes.unicode_minus'] = False  # 负号使用默认字体

""" 绘制线图(折线图/曲线图等)——matplotlib.pyplot.plot模块，线图适用场景：数据变化趋势 """

# 如果只有一个点，则无法显示，需要增加一个marker
# plt.plot([10], marker="o")

"""
# 绘制线段：x轴的数值默认是从0开始，单位为1
# 没有指定x轴数据，所以，就相当于绘制(0, 5)到(1, 10)再到(2, 5)的线段
# pyplot.plot()参数说明：
# color(c): 线段颜色
# linestyle(ls): 线段形状，比如--表示虚线，-表示实线
# linewidth(lw): 线段宽度
# marker: 绘制点展示，字母o表示实心圆，>或<表示箭头展示
# markerfacecolor(mfc): 绘制点颜色设置
# markersize(ms): 绘制点大小设置
# markeredgecolor(mec): 绘制点边缘颜色设置
# markeredgewidth(mew): 绘制点边缘宽度
# alpha: 透明度设置，默认为1，表示不透明
plt.plot([5, 10, 5], alpha=0.5, c='g', ls='--', lw=3, marker='o', mfc='b', ms=10, mec='r', mew=2)
plt.show()
"""

# 指定横纵坐标，第一个数组是x轴坐标，第二个数组是y轴坐标
# plt.plot([-1, 1, 1, -1, -1], [1, 1, -1, -1, 1])

# 分段绘制
# plt.plot([1, 2], [3, 4], "ro-.", [4, 2], [2, 3], "g<-")
# plt.plot([1, 2], [3, 4], "ro-.")
# plt.plot([4, 2], [2, 3], "g<-")

"""
# 绘制曲线(正弦曲线为例)
# matplotlib曲线绘制原理：matplotlib本身只能绘制线段。曲线和线段的关系：曲线是由无数多线段组成——参考圆内切多边形的思想
# 所以，当我们提供足够多的点，或者说两点之间距离足够短，那么绘制出来的线段就是曲线
# xs = np.linspace(0, 2 * np.pi, 10)
# xs = np.linspace(0, 2 * np.pi, 50)
xs = np.linspace(0, 2 * np.pi, num=100)
ys = np.sin(xs)
plt.plot(xs, ys)
# 通过pyplot.savefig()方法进行图像的保存
figure_name = "C:/Users/Administrator/Desktop/all/Temporary/" + str(int(time.time())) + ".png"
# plt.savefig(figure_name, dpi=200, facecolor="#BAA6C1")
plt.savefig(figure_name)
# 参数说明：dpi: 分辨率——每英寸有几个像素；facecolor: 背景色；bbox_inches: 是否紧凑保存
"""

"""
# matplotlib设置支持中文，直接在方法中设置是进行局部设置
mpl.rcParams['font.family'] = "SimHei"
mpl.rcParams['axes.unicode_minus'] = False  # 负号使用默认字体
xs = np.array([-1, -2, -3])
ys = np.array([4, 5, 6])
plt.plot(xs, ys)
plt.title("示例", fontfamily="Kaiti", fontsize=20)  # 就近原则，局部设置优先使用
"""
# plt.show()

"""
# 读取图像
from PIL import Image
image = Image.open("demo_sin.png")
print(image)
image.show()  # 使用系统图片查看程序打开图片文件
"""

"""
# 将图像保存到类文件对象(缓冲区)，并读取
from io import BytesIO
bio = BytesIO()
xs = np.linspace(0, 2 * np.pi, num=100)
ys = np.sin(xs)
plt.plot(xs, ys)
plt.savefig(bio)
bio.seek(0)
res = bio.read()
print(res)
"""

"""
# 图例
xs = np.arange(1, 13)
ys = np.random.randint(50, 70, size=(12,))
plt.plot(xs, ys, label="2017年")
ys = np.random.randint(50, 70, size=(12,))
plt.plot(xs, ys, label="2018年")

# 设置图例，pyplot.legend()参数说明：
# loc: 指定图例显示位置，如果没有指定，那么会根据最后生成的图像灵活调整
# loc可以传整数，也可以传元素个数为2的元组；整数1234分别代表右上/左上/左下/右下，
# 0表示最佳位置即根据最后生成的图像灵活调整，元组指定基于图像尺寸偏移比例
# frameon: 是否需要图例边框，默认为True
# title: 标题设置
# ncol: 图例显示列数，默认为1
plt.legend(loc=(1, 1), frameon=False, title='年份', ncol=1)

# 网格线
# color(r): 网格线颜色设置
# axis: 网格线x/y轴显示控制，默认为both即都显示
# linestyle(ls): 网格线形状设置
# linewidth(lw): 网格线宽度设置
# plt.grid(c='r', axis='y', ls='-.', lw=2)
plt.grid(ls='-.')
plt.show()
"""


# 绘图区域，其实上面使用pyplot.plot()直接绘制图像，也会隐式先去创建一个figure对象，figure对象理解为画布，是matplotlib的基础
# pyplot.figure().add_subplot(x, y, index)，x、y表示绘图区域按照几行几列展示，index是索引从“1”开始
# canvas = plt.figure()
# area1 = canvas.add_subplot(2, 2, 1)
# area1.plot([1, 2, 3], [4, 5, 6])
# area2 = canvas.add_subplot(2, 2, 2)
# area2.plot([1, 2, 1], [4, 5, 6])
# area3 = canvas.add_subplot(2, 2, 3)
# area3.plot([1, 2, 1], [7, 8, 9], marker='o', ls='')

# plt.subplots_adjust(wspace=10, hspace=3)  # 绘图区域间隙设置

# pyplot.subplots(x, y)返回一个元组：第一个返回值为figure对象，第二个为绘图区域数组———推荐做法！sharex=True, sharey=True进行共享x/y轴，默认是不共享的
fig, areas = plt.subplots(2, 2, sharex=True, sharey=True)
fig.set_size_inches(3, 3)  # 通过figure对象的set_size_inches()方法设置绘图区域长宽比
areas[0][0].plot([1, 2, 3], [4, 5, 6])
areas[1][1].plot([4, 5, 6], [10, 20, 30])

plt.gcf().set_size_inches(3, 5)  # pyplot.gcf()方法意为：get current figure，即返回当前使用的figure对象

plt.show()







