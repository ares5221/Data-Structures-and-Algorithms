#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as line
import random
import math


# 对应博客算法5
def GeneratePointInTriangle1(point_num, pointA, pointB, pointC):
    for i in range(1, point_num + 1):
        u = random.uniform(0.0, 1.0)
        v = random.uniform(0.0, 1.0 - u)
        pointP = u * pointC + v * pointB + (1.0 - u - v) * pointA;
        plt.plot(pointP[0], pointP[1], '*', color="black")


# 根据向量叉乘计算三角形面积，参考 http://www.cnblogs.com/TenosDoIt/p/4024413.html
def ComputeTriangleArea(pointA, pointB, pointC):
    return math.fabs(np.cross(pointB - pointA, pointB - pointC)) / 2.0


# 判断点P是否在三角形ABC内,参考 http://www.cnblogs.com/TenosDoIt/p/4024413.html
def IsPointInTriangle(pointA, pointB, pointC, pointP):
    area_abc = ComputeTriangleArea(pointA, pointB, pointC)
    area_pab = ComputeTriangleArea(pointA, pointB, pointP)
    area_pbc = ComputeTriangleArea(pointP, pointB, pointC)
    area_pac = ComputeTriangleArea(pointP, pointA, pointC)
    return math.fabs(area_pab + area_pac + area_pbc - area_abc) < 0.000001


# 计算一个点关于某一点的中心对称点
def ComputeCentralSymmetryPoint(point_src, point_center):
    return np.array([point_center[0] * 2 - point_src[0], point_center[1] * 2 - point_src[1]])


# 对应博客算法6
def GeneratePointInTriangle2(point_num, pointA, pointB, pointC):
    for i in range(1, point_num + 1):
        pointP = np.array([random.uniform(pointA[0], pointB[0]), random.uniform(pointA[1], pointC[1])])
        if not IsPointInTriangle(pointA, pointB, pointC, pointP):
            if pointP[0] > pointC[0]:
                pointP = ComputeCentralSymmetryPoint(pointP, np.array(
                    [(pointC[0] + pointB[0]) / 2, (pointC[1] + pointB[1]) / 2]))
            else:
                pointP = ComputeCentralSymmetryPoint(pointP, np.array(
                    [(pointC[0] + pointA[0]) / 2, (pointC[1] + pointA[1]) / 2]))
        plt.plot(pointP[0], pointP[1], '.', color="blue")


fig = plt.figure()
# 三角形三个顶点
pointA = np.array([0, 1])
pointB = np.array([3, 1])
pointC = np.array([1, 2])

plt.plot([pointA[0], pointB[0]], [pointA[1], pointB[1]])
plt.plot([pointA[0], pointC[0]], [pointA[1], pointC[1]])
plt.plot([pointB[0], pointC[0]], [pointB[1], pointC[1]])

GeneratePointInTriangle2(1500, pointA, pointB, pointC)  # 修改此处来显示不同算法的效果

plt.ylim(0.5, 2)
plt.xlim(0, 3)
plt.show()