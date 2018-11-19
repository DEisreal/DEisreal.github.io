# -*- coding: UTF-8 -*-
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

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

#ω=π x1(t)=sin(ωt)u(t)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(ω*x)*u(k,0)

plt.figure("x1(t)=sin(ωt)u(t)")
plt.plot(x,y)

#ω=π t0=1 x2(t)=sin(ω(t-t0)u(t)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(ω*(x-t0))*u(k,0)

plt.figure("x2(t)=sin(ω(t-t0)u(t)")
plt.plot(x,y)

#ω=π t0=-1 x3(t)=sin(ωt)u(t-t0)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(np.pi*x)*u(k,t0)

plt.figure("x3(t)=sin(ωt)u(t-t0)")
plt.plot(x,y)

#ω=π t0=-1 x4(t)=sin(ω(t-t0)u(t-t0)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(np.pi*(x-t0))*u(k,t0)

plt.figure("x4(t)=sin(ω(t-t0)u(t-t0)")
plt.plot(x,y)
plt.show()