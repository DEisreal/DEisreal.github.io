# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots() 
#建立一个fig对象，建立一个axis1对象
ax = plt.gca() 
#获取ax图例Convolution signal process
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
ax.set(xlim=[-15, 15], ylim=[0, 6], title='卷积信号动画演示',
       ylabel='Y-轴', xlabel='X-轴')
#设置x轴y轴范围及标题
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#隐藏轴上边和右边
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
#获取指定的x区间的数据
ω=np.pi/4
x = np.linspace(-10, 0, 1000)
x1 = np.linspace(-13, -8, 1000)
x_data, y_data = [], []
y = 4*np.sin(ω*x)        #控制固定函数
y[0] = 0
y[-1] = 0
ax.plot(x, y, "red")
def init():
    y1 = 2*np.sin(x1)
    line.set_data(x1,y1)
    return line,
def animate(i):
    x2 = np.linspace(-13 + i, -8 + i, 1000)
    y2 = x1/x1            #控制卷积函数
    y2[0] = 0
    y2[-1] = 0
    line.set_data(x2,y2)
    if i == 0:
        global x_data, y_data
        x_data, y_data = [], []
        line1, = ax.plot(x_data, y_data, "yellow")

    if  i >= 6 and i < 8:
        x_data.append(-8+i)
        y_data.append(2*(-8+i)+2)
        line1, = ax.plot(x_data, y_data, "yellow")
      
        return line, line1,
    if i >= 8 and i < 11:
        x_data.append(-8+i)
        y_data.append(4)
        line1, = ax.plot(x_data, y_data, "yellow")

        return line, line1,
    elif i >= 11:
        x_data.append(-8+i)
        y_data.append(2*(4-(-8+i)))
        line1, = ax.plot(x_data, y_data, "yellow")
        return line, line1,

    return line,

y3 = 2*np.sin(x1)
y3[0] = 2
y3[-1] = 0
line, = ax.plot(x1, y3, "black")    #控制移动函数


anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=100, blit=True) 
#30帧的动画并且帧与帧之间间隔100ms，blit是一个非常重要的关键字，它告诉动画只重绘修改的部分，结合上面保存的时间， blit=true会使动画显示得会非常非常快


plt.show()