# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""画sin、arcsin、cos、arccos、tan、arctan 图片"""


import matplotlib.pyplot as plt
import numpy as np

# 1. 画sin、arcsin、cos、arccos

plt.figure(figsize=(5, 5))

x1 = np.linspace(-np.pi / 2, np.pi / 2)
y1 = np.sin(x1)
plt.plot(x1, y1, label="f(x) = sin(x)")

x2 = np.linspace(-1, 1, 500)
y2 = np.arcsin(x2)
plt.plot(x2, y2, label="f(x) = arcsin(x)")

x3 = np.linspace(0, np.pi, 500)
y3 = np.cos(x3)
plt.plot(x3, y3, label="f(x) = cos(x)")

x4 = np.linspace(-1, 1, 500)
y4 = np.arccos(x4)
plt.plot(x4, y4, label="f(x) = arccos(x)")

plt.legend()
plt.show()

# 2. 画tan、arctan

plt.figure(figsize=(5, 5))
lim = 8
plt.ylim(-lim, lim)
plt.xlim(-lim, lim)

x5 = np.linspace(-np.pi / 2, np.pi / 2, 500)
y5 = np.tan(x5)
plt.plot(x5, y5, label="f(x) = tan(x)")

x6 = np.linspace(-lim, lim, 500)
y6 = np.arctan(x6)
plt.plot(x6, y6, label="f(x) = arctan(x)")

plt.legend()
plt.show()