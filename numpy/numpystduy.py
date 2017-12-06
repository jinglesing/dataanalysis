# -*- coding: utf-8 -*-
"""
numpy  切片 索引 功能函数 运算 操作

Created on Wed Dec  6 10:33:15 2017

@author: singlejing
"""
import numpy as np

#reshape不改变原数组元素，返回一个shape形状数组，resize改变数组和reshape其余功能一样
a = np.arange(1,25).reshape(2,3,4)
print (a)
#[[[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
#
# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]]

#轴 秩
print (a.ndim)
#形状(2, 3, 4)
print (a.shape)
#size24
print (a.size)
#dtype int32
print (a.dtype)
#每一个元素的大小，字节 4
print (a.itemsize)

#创建一个n*n的矩阵d对角线为1其余为0
print(np.eye(10))

#根据起始位置等间距的填充数组,endpoint是否用最后一个值
print("linspace is :{}".format(np.linspace(1,12,4,endpoint=True)))

#将维度调换
print("swapaxes( is :{}".format(np.swapaxes(a,0,1)))

#将高维数组将为一维，只是拷贝，原数组不变
print(a.flatten())

#将数组的元素数据类型改变
print(a.astype(float))


# 数组向列表的转换
print(a.tolist())

print(np.ones((2,3,4),dtype=np.int))
print(np.zeros((2,3,4)))
print(np.full((2,3,4),4.))
print(np.ones_like(a))
print(np.zeros_like(a))
print(np.full_like(a,8.8))



#切片
print (a[:,:,1:3])

#[[[ 2  3]
#  [ 6  7]
#  [10 11]]
#
# [[14 15]
#  [18 19]
#  [22 23]]]
print (a[1:2,:,1:3])

#[[[14 15]
#  [18 19]
#  [22 23]]]


print("")

b = np.sqrt(a)
print (b)

c = np.square(a)
print (c)

#返回两个数组一个整数部分一个小数部分
d = np.modf(a)
print (d)

#比较a,b返回bool值ndarray
e = a == b
print (e)

f = np.rint(b)
print (f)
h = 1/a
g = np.cos(h)
i = np.cosh(h)
print ('cos is:{}'.format(g))
print ("cosh is:{}".format(i))
print ("exp is: {}".format(np.exp(a)))

#计算平均值 绝对值 
b = np.mean(a)
print ("mean is: {}".format(b))
c = np.arange(-10,100)
print ("abs is: {}".format(np.abs(c)))
#ceil表示大于元素的整数值floor 小于元素的整数值
print ("ceiling is: {}".format(np.ceil(c)))
print ("floor is: {}".format(np.floor(c)))
#a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
#np.floor(a)
#array([-2., -2., -1.,  0.,  1.,  1.,  2.])

a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
b = np.array([1,2,3,5,6,7,8])
print ("rint is: {}".format(np.rint(a)))#元素四舍五入
print ("sign is: {}".format(np.sign(a)))#元素 的符号值
print ("exp is: {}".format(np.exp(b)))#元素的指数值
print (a,b)

print ("mod is: {}".format(np.mod(a,b)))#元素级的取模
print ("copysign is: {}".format(np.copysign(a,b)))#元素的符号赋值
print (a,b)






