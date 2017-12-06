# -*- coding: utf-8 -*-
"""
CSV文件存取、多维数据存储可以通过元数据文件来存储额外信息
Created on Wed Dec  6 20:49:01 2017

@author: Administrator
"""
import numpy as np
#多维数组要降维度之后再保存
b = np.arange(24).reshape(2,3,4)
a = np.arange(24)
np.savetxt("D:/numpyy/hello.csv",a,fmt="%d",delimiter=None)
b.tofile("D:/numpyy/hellob.csv",sep=",",format="%s")

#读取文件内的内容count=-1代表读取整个文件(读入个数)sep数据分割字符串如果是空串写入文件为二进制
c = np.fromfile("D:/numpyy/hellob.csv",dtype =np.int,count =-1,sep=",")
print(c)
c = np.fromfile("D:/numpyy/hellob.csv",dtype =np.int,count =-1,sep=",").reshape(2,3,4)
print(c)


#使用save和load时要注意文件后缀是.npy
np.save("d:/numpyy/helloc.csv",b)
d = np.load("d:/numpyy/helloc.csv.npy")
print (d)