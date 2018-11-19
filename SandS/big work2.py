# -*- coding: UTF-8 -*-
#coding=utf-8

import numpy as np
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt

face=misc.face(gray=True) #创建一个灰度图像
scharr=np.array([[-3-3j,0-10j,+3-3j],
        [-10+0j,0+0j,+10+0j],
         [-3+3j,0+10j,+3+3j]]) #设置一个特殊的卷积和
grad=signal.convolve2d(face,scharr,boundary='symm',mode='same') #把图像的face数组和设计好的卷积和作二维卷积运算,设计边界处理方式为symm
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,6)) #建立1行2列的图fig
ax1.imshow(face,cmap='gray') #显示原始的图
<matplotlib.image.AxesImage object at 0x00000000078FC198>
 ax1.set_axis_off() #不显示坐标轴
 ax2.imshow(np.absolute(grad),cmap='gray') #显示卷积后的图
<matplotlib.image.AxesImage object at 0x00000000078FCE48>
 ax2.set_axis_off() #不显示坐标轴
fig.show() #显示绘制好的画布