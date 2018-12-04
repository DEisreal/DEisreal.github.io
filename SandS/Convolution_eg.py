# -*- coding: UTF-8 -*-
#coding=utf-8


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

import matplotlib.pyplot as plt
import numpy as np 

#连续卷积试用

def()
#x(t)
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
t = np.linspace(0, 3 * np.pi, 100)
x = np.sin(t)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
plt.title(r'$x(t)=sin(t)$') 
plt.plot(t, x)
#plt.show()

#h(t)
t1 = [z*0.375*np.pi for z in t]
h = np.sin(t1)
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$h(t)=sin(\omega t), \omega = \frac{3}{8} \pi$') 
plt.plot(t1, h)
plt.show()

#y(t)

y = np.convolve(x,h,'full') #卷积运算
plt.subplot(2,1,1)
plt.title(r'$y(t)=x(t)*h(t)$') 
plt.plot(y)
print(y)
plt.show()