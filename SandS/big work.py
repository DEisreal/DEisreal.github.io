# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

def u(t,t0):
    n=0
    for i in t:
        if(i<t0):
           t[n]=0
           n+=1
        else:
           t[n]=1
           n+=1
    return t
x0=-1
x1=np.pi
ω=np.pi
t0=1

#x(t)
x=np.linspace(x0,x1,100)
a=np.linspace(x0,x1,100)
y=np.sin(ω*x)*u(a,0)
plt.subplot(1,2,1)
plt.title("x(t)=sin(ωt)u(t)") 
plt.plot(x,y)
#h(t)
z=np.linspace(x0,x1,100)
y1=np.sin(z)
plt.subplot(1,2,2)
plt.title("h(t)=sin(t)") 
plt.plot(z,y1)

#时域的卷积=频域的乘积,所以用傅里叶变换快速实现卷积_fft

#scipy.signal.fftconvolve    
#使用快速傅里叶变换卷积函数。
#scipy.linalg.toeplitz 
#可用于构造卷积运算符（Used to construct the convolution operator.）。
#polymul 
#多项式乘法，可以同本函数获得相同的输出，但是还可以接受poly1d对象作为输入。

#a:(N,)输入的一维数组
#b:(M,)输入的第二个一维数组
#　mode:{‘full’, ‘valid’, ‘same’}参数可选
#　　　‘full’　默认值，返回每一个卷积值，长度是N+M-1,在卷积的边缘处，信号不重叠，存在边际效应。
#　　　‘same’　返回的数组长度为max(M, N),边际效应依旧存在。
#　　　‘valid’ 　返回的数组长度为max(M,N)-min(M,N)+1,此时返回的是完全重叠的点。边缘的点无效。

b=np.convolve(y,y1)
plt.figure("卷积")
plt.title("y(t)——Y(jw)；X(jw)*Y(jw)——x(t)·h(t)") 
plt.plot(b)
plt.show()



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