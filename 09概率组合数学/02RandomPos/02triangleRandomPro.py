#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt
import random, math

x_values = []
y_values = []
A = [0, 1]
B = [3, 1]
C = [1, 2]
for i in range(10000):
    t = random.random()
    s = random.random()
    a = 1 - math.sqrt(t)
    b = (1 - s) * math.sqrt(t)
    c = s * math.sqrt(t)
    xx = a * A[0] + b * B[0] + c * C[0]
    yy = a * A[1] + b * B[1] + c * C[1]
    x_values.append(xx)
    y_values.append(yy)

'''
scatter() 
x:横坐标 y:纵坐标 s:点的尺寸
'''
plt.scatter(x_values, y_values, s=4)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 3, 1, 2])
plt.show()
