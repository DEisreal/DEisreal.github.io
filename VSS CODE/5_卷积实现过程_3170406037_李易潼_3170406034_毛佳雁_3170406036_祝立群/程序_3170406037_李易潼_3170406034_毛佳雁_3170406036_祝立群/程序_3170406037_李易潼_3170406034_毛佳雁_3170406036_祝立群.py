# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
plt.rcParams['animation.convert_path'] = 'D:\RouseWeiser\ImageMagick-6.2.7-Q16\convert.exe'

fig, ax = plt.subplots() 
#建立一个fig对象，建立一个axis1对象
ax = plt.gca() 
#获取ax图例Convolution signal process
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
ax.set(xlim=[-5, 5], ylim=[0, 2.5], title='Envolved signal animation presentation',
       ylabel='Y-axis', xlabel='X-axis')
#设置x轴y轴范围及标题
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#隐藏轴上边和右边
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
#获取指定的x区间的数据

x = np.linspace(-1, 1, 1000)
x1 = np.linspace(-8, 1, 1000)
x_data, y_data = [], []
y = x1/x1        #控制固定函数
y[0] = 0
y[-1] = 0
ax.plot(x, y, "red")
def init():
    y1 = x1/x1
    line.set_data(x1,y1)
    return line,
def animate(i):
    x2 = np.linspace(-4 + i, -2 + i, 1000)
    y2 = x1/x1            #控制卷积函数
    y2[0] = 0
    y2[-1] = 0
    line.set_data(x2,y2)
    if i == 0:
        global x_data, y_data
        x_data, y_data = [], []
        line1, = ax.plot(x_data, y_data)

    if  i>=-3 and i < 1:
        x_data.append(i - 4)
        y_data.append(2+(i - 4))
        line1, = ax.plot(x_data, y_data, "yellow")
        return line, line1,

    elif  i >= 1:
        x_data.append(i - 1)
        y_data.append(2-(i - 1))
        line1, = ax.plot(x_data, y_data, "yellow")
        return line, line1,

    return line,

y3 = x1/x1
y3[0] = 2
y3[-2] = 0
line, = ax.plot(x1, y3, "black")    #控制移动函数

# call the animator.  blit=true means only re-draw the parts that have changed.
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=1000, blit=True) 
anim1.save('exxxo.gif', fps=2, writer='imagemagick')
plt.show()
