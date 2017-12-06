# -*- coding: utf-8 -*-
"""
统计类函数
Created on Wed Dec  6 18:53:30 2017

@author: Administrator
"""
import numpy as np
a = np.arange(24).reshape(2,3,4)
print (a)
print("sum is:{}".format(np.sum(a)))

print("mean is:{}".format(np.mean(a)))

#给定轴加权平均数，1为列2为行
print("average is:{}".format(np.average(a,axis=2,weights=(10,1,1,1))))

#给定轴算标准差
print("std is :{}".format(np.std(a,axis=None)))

#给定轴算方差
print ("var is {}".format(np.var(a,axis=1)))

a = np.array([[1,3,2,66,34,23],[32,33,34,35,23,33]])
print (a)
print ("min is {}".format(np.min(a,axis=None)))
print ("max is {}".format(np.max(a,axis=None)))

#降一维下标的最小值最大值,扁平化后的下标
print ("argmin is {}".format(np.argmin(a,axis=None)))
print ("argmax is {}".format(np.argmax(a,axis=None)))

#降一维下标index转换为多维下标
print ("unravel_index is {}".format(np.unravel_index(np.argmax(a),a.shape)))

#计算数组a中元素的最大值和最小值之差
print("ptp is :{}".format(np.ptp(a)))

#计算数组a中元素的中值（中位数）
print("median is :{}".format(np.median(a)))

#梯度的概念
#左边减右边值的平均数，边界值就减一边不除二
b = np.random.randint(100,200,(5))
print(b)
print("gradient is :{}".format(np.gradient(b)))
#多维梯度会打印多行梯度的，下面就会各自输出两个维度的梯度
b = np.random.randint(100,200,(5,3))
print(b)
print("gradient is :{}".format(np.gradient(b)))





