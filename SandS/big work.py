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
