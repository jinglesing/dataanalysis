# -*- coding: utf-8 -*-
"""
图像操作使用PIL Image numpy

Created on Wed Dec  6 22:17:31 2017

@author: jinglesing
"""

from PIL import Image
import numpy as np
im = np.array(Image.open("d:/numpyy/hello.jpg"))

print(im.shape,im.dtype)
#(2448, 3264, 3) uint8 图像是一个三维数组分别是高度、宽度、像素RGB
#a = np.array(Image.open("d:/numpyy/cRonaldo.jpg"))
#print(a.shape,a.dtype)
#b = [255,255,255]-a
#im = Image.fromarray(b.astype("uint8"))
#im.save("d:/numpyy/cR1.jpg")

a = np.array(Image.open("d:/numpyy/cRonaldo.jpg").convert("L"))#convert("L")取灰度
print (a.dtype)
print (a)
b= 255 -a
print (b)
im = Image.fromarray(b.astype("uint8"))
im.save("d:/numpyy/cR2.jpg")

a = np.array(Image.open("d:/numpyy/cRonaldo.jpg").convert("L"))#convert("L")取灰度
print (a.dtype)
print (a)
b= 255*(a/255)**2#像素平方
print (b)
im = Image.fromarray(b.astype("uint8"))
im.save("d:/numpyy/cR3.jpg")

a = np.array(Image.open("d:/numpyy/cRonaldo.jpg").convert("L"))#convert("L")取灰度
print (a.dtype)
print (a)
b= (100/255)*a+150#区间变换
print (b)
im = Image.fromarray(b.astype("uint8"))
im.save("d:/numpyy/cR4.jpg")