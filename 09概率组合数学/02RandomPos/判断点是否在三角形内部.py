#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
随机生成1000个点，选取任意3个点组成三角形，问，如何判断其余的997个点在三角形内或外？
'''
import numpy as np
import random

# 定义点
class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("x坐标：%s,y坐标：%s" % (self.x, self.y))
        # "Freind : %s" %self.name 返回多个参数啊


# 定义三角形
class Triangle(object):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return ("A点：%s B点：%s C点：%s" % (self.A, self.B, self.C))

    # 判断构建的三角形是否满足三角形条件，即面积是否为零
    def isTriangle(self):
        arr = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        s = abs(0.5 * np.linalg.det(arr))
        return False if s == 0 else True

    # 判断一个点是否在三角形内，即该点与三角形任意两点构成的面积不为0且面积和为外部大三角形面积之和
    def isInTriangle(self, D):
        arr1 = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        sumAera = 0.5 * np.linalg.det(arr1)
        arr2 = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [D.x, D.y, 1]])
        s1 = 0.5 * np.linalg.det(arr2)
        arr3 = np.array([[self.A.x, self.A.y, 1], [D.x, D.y, 1], [self.C.x, self.C.y, 1]])
        s2 = 0.5 * np.linalg.det(arr3)
        arr4 = np.array([[D.x, D.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        s3 = 0.5 * np.linalg.det(arr4)
        if s1 != 0 and s2 != 0 and s3 != 0 and abs(s1 + s2 + s3 - sumAera) < 0.000001:
            return True
        else:
            return False


if __name__ == '__main__':
    # 产生1000个点且存储起来
    arrOfVertex = []
    for i in range(1000):
        tempx = random.randint(1, 100)
        tempy = random.randint(1, 100)
        tempVertex = Vertex(tempx, tempy)
        arrOfVertex.append(tempVertex)
    # 在这1000个点中随机选取3个点且保证这三个点构成一个三角形
    k, j, m = random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)
    selectedTriangle = Triangle(arrOfVertex[k], arrOfVertex[j], arrOfVertex[m])
    while not selectedTriangle.isTriangle():
        k, j, m = random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)
        selectedTriangle = Triangle(arrOfVertex[k], arrOfVertex[j], arrOfVertex[m])
    # 判断点是否在三角形中，且用一个数组存储起来
    arrOfJudge = []
    sum = 0
    for i in range(1000):
        temp = selectedTriangle.isInTriangle(arrOfVertex[i])
        print(arrOfVertex[i], end="  ")
        if temp: sum += 1
        arrOfJudge.append(temp)
    print("选取的是否为三角形:%s" % selectedTriangle.isTriangle())
    print(arrOfJudge)
    print("在三角形内部的比例为：%s %%" % (sum / 10))
# a = Vertex(1, 1)
# b = Vertex(2, 2)
# c = Vertex(3, 3)
# print(a)
# tri = Triangle(a, b, c)
# print(tri)
# print(tri.isTriangle())
