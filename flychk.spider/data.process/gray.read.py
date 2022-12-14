#原始数据是二维图像,横轴是时间，纵轴是位置坐标，像素值代表的是X射线的强度大小。

#包的调用
import cv2  #openCV，python处理图像的常用包,注意工作路径必须是全英文
import csv  #检视生成的灰度矩阵
import matplotlib.pyplot as plt
import pylab
import os   #判断python工作路径
import pandas as pd  #数据保存
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#读取图像
print(os.getcwd())#读取路径
img=cv2.imread('./flychk.spider/data.process/sFFs.data/carbon/202001203002-SR-FFS-Grating 13.8 mm-Slit 30 um-Al 0.75 um.tiff',cv2.IMREAD_GRAYSCALE)#获取图像
type(img)
print(img)

#创建窗口并显示图像
cv2.namedWindow('carbon',cv2.WINDOW_NORMAL)
cv2.imshow('carbon',img)
cv2.imwrite('gray.png',img)#保存为.png图像

#保存灰度图像为矩阵进行检视
carbon_gray_array=np.array(img)
carbon_gray_df=pd.DataFrame(carbon_gray_array)
carbon_gray_df.to_csv('carbon_gray.csv')#注意：此时csv中保存了矩阵的位置序号


#数据处理
#可能会涉及对数据的归一化处理？



#首先要计算确定旋转的角度，
#使用二值化来处理图像？

#处理完成之后随机选取一个z位置进行强度曲线的处理
#一维是实际空间成像，一维是色散开的光谱

#两个问题：如何确定波长的位置？如何知道纵向上两点之间的距离？
#刘运全

#1.标准工作模式的参数：
#2.根据光谱中谱线的半高宽以及响铃谱线的分辨情况，可以得到谱仪的分辨率


#确定旋转角度angle
#########################建议后续再来开发有关于旋转角度确定的算法，现在应该将主要的精力集中在平场光谱本身的物理机制上
#def angle_calculation(img):
    #retval是得到的阈值，img_2是得到的二值化图像
#    retval,img_2=cv2.threshold(img,10,255,cv2.THRESH_BINARY)
#    cv2.imwrite('binary.png',img_2)
    #一种被允许的处理思路：可以忽略像差引起的辉光，而将其作为有意义的数据进行处理

#    return img_2

#img_binary=angle_calculation(img)
#cv2.namedWindow('carbon_binary',cv2.WINDOW_NORMAL)#创建窗口
#cv2.imshow('carbon_binary',img_binary)#显示二值化处理后的图像


#初步方法：利用人眼进行人工数值迭代确定，找到最佳旋转角度
#定义旋转图片操作
def rotate(image,angle,center=None,scale=1.0):
    #获取图像分辨率
    (h,w)=image.shape[:2]

    #默认图像中心
    if center is None:
        center=(w//2,h//2)
    
    #执行旋转操作
    M=cv2.getRotationMatrix2D(center,angle,scale)
    img_rotated=cv2.warpAffine(image,M,(w,h))

    #返回执行结果
    return img_rotated


#执行旋转操作并且给出对应的图像
#猜测旋转角度
angle_guess=0.55#这个值是针对于碳参考平面图而言的，之后的涉及大量的图像处理还是要用到旋转角度识别算法
img_rotated=rotate(img,angle_guess,None)
cv2.namedWindow('carbon_rotated',cv2.WINDOW_NORMAL)#创建窗口
cv2.imshow('carbon_rotated',img_rotated)#显示二值化处理后的图像

#软X射线经过衍射光栅进行分光，从而形成谱图
#软X射线的波段：1.0nm到30.0纳米
#平场光谱仪实际上是通过时间尺度的扫描来得到不同波长的强度
#也就是说，之前所说的横轴是时间尺度从实际意义上来说没错，但是真正的物理意义仍然是波长，
#或者说是频率

#窗口管理
k=cv2.waitKey(0)# 0代表无限等待键盘输入
#定义esc为退出图像键
if k==27:
    cv2.destroyAllWindows()

