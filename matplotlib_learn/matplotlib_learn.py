# coding:utf8
import time
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a, b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
figure_name = str(int(time.time()))
plt.savefig("/data/matplotlib/" + figure_name + ".png")
# plt.show()
