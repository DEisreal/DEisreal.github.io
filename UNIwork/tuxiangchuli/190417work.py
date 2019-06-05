# -*- coding: UTF-8 -*-
#coding=utf-8


import cv2
import numpy as np
import matplotlib.pyplot as plt 
# theme: 车牌识别

def imread_photo(filename,flags = cv2.IMREAD_COLOR ):
    # 该函数能够读取磁盘中的图片文件，默认以彩色图像的方式进行读取    
    # 输入： filename 指的图像文件名（可以包括路径）          
    # flags用来表示按照什么方式读取图片，有以下选择（默认采用彩色图像的方式）：              
    # IMREAD_COLOR 彩色图像           
    # IMREAD_GRAYSCALE 灰度图像              
    # IMREAD_ANYCOLOR 任意图像    
    # 输出: 返回图片的通道矩阵     
    return  cv2.imread(filename,flags)   
    
if __name__ == "__main__":    
    img = imread_photo("D:/世界/修理工/脑浆炸裂/数字图像处理2019.03/04.17作业/car.jpg")    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    cv2.imshow('img',img)    
    cv2.imshow('gray_img', gray_img)    
    cv2.waitKey(0)    
    cv2.destroyAllWindows()

def resize_photo(imgArr,MAX_WIDTH = 1000):    
    # 这个函数的作用就是来调整图像的尺寸大小，当输入图像尺寸的宽度大于阈值（默认1000），我们会将图像按比例缩小    
    # 输入： imgArr是输入的图像数字矩阵    
    # 输出:  经过调整后的图像数字矩阵    
    # 
    # 拓展：OpenCV自带的cv2.resize()函数可以实现放大与缩小，函数声明如下：
    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst        
    # 其参数解释如下：            
    # src 输入图像矩阵            
    # dsize 二元元祖（宽，高），即输出图像的大小            
    # dst 输出图像矩阵            
    # fx 在水平方向上缩放比例，默认值为0            
    # fy 在垂直方向上缩放比例，默认值为0            
    # interpolation 插值法，如INTER_NEAREST，INTER_LINEAR，INTER_AREA，INTER_CUBIC，INTER_LANCZOS4等
    img = imgArr    
    rows, cols= img.shape[:2]     
    #获取输入图像的高和宽    
    if cols >  MAX_WIDTH:        
        change_rate = MAX_WIDTH / cols
        img = cv2.resize(img ,( MAX_WIDTH ,int(rows * change_rate) ), interpolation = cv2.INTER_AREA)
        return img

    
