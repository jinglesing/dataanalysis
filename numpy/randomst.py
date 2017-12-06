# -*- coding: utf-8 -*-
"""
numpy随机数的学习
返回数据大多数默认浮点型
Created on Wed Dec  6 16:19:57 2017

@author: Administrator
"""

import numpy as np

#浮点数，[0,1)，均匀分布
a = np.random.rand(2,3,4)
print ("rand is:{}".format(a))

#标准正态分布
b = np.random.randn(2,3,4)
print ("randn is:{}".format(b))

#随机整数根据范围加shape
c = np.random.randint(100,200,(3,4))
print ("randint is:{}".format(c))

#seed种子,可以固定不变
np.random.seed(10)

print ("seed randint is:{}".format(c))
np.random.seed(10)
print ("seed randint is:{}".format(c))

#shuffle,数组c的第一轴进行跑咧===并且改变了原数组
np.random.shuffle(c)
print ("shuffle randint is:{}".format(c))

#和shuffle一样但不改变原数组
d = np.random.randint(100,200,(3,4))
np.random.permutation(d)
print ("permutation randint is:{}".format(d))

#choice 对一维数组按概率取随机数，并可以形成新的数组
b = np.random.randint(100,200,(8))
print ("b is:{}".format(b))
print ("choice is:{}".format(np.random.choice(b,(3,2),replace=False)))
print ("choice+p is:{}".format(np.random.choice(b,(3,2),replace=False,p=b/np.sum(b))))

print ("b is:{}".format(b))

#uniform 均匀分布 起始值 结束值 形状
print ("uniform is ；{}".format(np.random.uniform(100,200,(10))))
#normal 正态分布 均值 方差 形状
print ("normal is ；{}".format(np.random.normal(100,0.15,(10))))
#poisson 泊松分布 随机事件发生率 形状
print ("poisson is ；{}".format(np.random.poisson(0.8,(10))))

