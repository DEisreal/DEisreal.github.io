# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50

#x1(t)
x1 = np.linspace(0, 3 * np.pi, 100)
y1 = np.sin(x1)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(2,1,1)
plt.title(r'$x1(t)=sin(\omega x)u(t)$') 
plt.plot(x1, y1)
plt.show()