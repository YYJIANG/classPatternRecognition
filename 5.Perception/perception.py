# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:53:36 2021

@author: JYY
"""

'''
蓝色线为原始分割线，橙色线为感知机输出分割线。
'''


import numpy as np
from matplotlib import pyplot as plt


N = 50                  # 样本数
lr = 1                  # 学习率
epoch_num = 1000        # 最大迭代次数

# 初始化样本
samples = np.zeros((N,3))
plt.axis([0,1,0,1])

# N个随机2维数据,每个维度取值[0,1)
rd = np.random.rand(N,2)
for i in range(N):
    for j in range(2):
        samples[i,j] = rd[i,j]
# 生成斜率随机、过点(0.5, 0.5)的直线，将数据分为线性可分的2类
k = np.tan((np.random.rand()-1)*np.pi)
line_x = np.linspace(0,1,50)
line_y = k*(line_x-0.5)+0.5
plt.plot(line_x,line_y,'cornflowerblue')
# 在直线上方为红色，在直线下方为绿色
for i in range(N):
    samples[i,2] = 1 if samples[i,1]>(samples[i,0]-0.5)*k+0.5 else -1
    plt.scatter(samples[i,0],samples[i,1], c='red' if samples[i,2]==1 else 'green')

# 初始化权重w，b
w = np.random.rand(2)
b = np.random.rand()

for epoch in range(epoch_num):
    err = []
    for i in range(N):
        if -samples[i,2]*(w[0]*samples[i,0]+w[1]*samples[i,1]+b) > 0 :
            err.append(i)
    if err==[]:
        break
    grad_w = np.zeros(2)
    grad_b = 0
    for i in err:
        grad_w[0] -= samples[i,2]*samples[i,0]
        grad_w[1] -= samples[i,2]*samples[i,1]
        grad_b -= samples[i,2]
    w = w-lr*grad_w
    b = b-lr*grad_b


line_w = np.linspace(0,1,50)
line_yy = -(w[0]*line_w+b)/w[1]
plt.plot(line_w,line_yy,'darkorange')
plt.show()
print('Number of epoch: ',epoch)


