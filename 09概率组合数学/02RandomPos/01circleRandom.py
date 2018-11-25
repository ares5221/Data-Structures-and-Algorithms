#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt
import random, math
x_values = []
y_values = []
'''
#会造成中心过度集中的情况
for i in range(1000):
    r = random.randint(0,100) - 50
    theta = random.randrange(0,10000)
    x_values.append(r* math.cos(theta))
    y_values.append(r * math.sin(theta))

# print(r,theta)
# print(theta)
'''
for i in range(1000):
    x = random.randint(0,100) - 50
    y = random.randint(0, 100) - 50
    if x*x + y*y < 50*50:
        x_values.append(x)
        y_values.append(y)

'''
scatter() 
x:横坐标 y:纵坐标 s:点的尺寸
'''
plt.scatter(x_values, y_values, s=4)

# 设置图表标题并给坐标轴加上标签
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([-60, 60, -60, 60])
plt.show()