#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
def RadixSort(ls):
    def getbit(x, i):  # 返回x的第i位（从右向左，个位为0）数值
        y = x // pow(10, i)
        z = y % 10
        return z

    def CountSort(ls):
        n = len(ls)
        num = max(ls)
        count = [0] * (num + 1)
        for i in range(0, n):
            count[ls[i]] += 1
        arr = []
        for i in range(0, num + 1):
            for j in range(0, count[i]):
                arr.append(i)
        return arr

    Max = max(ls)
    for k in range(0, int(math.log10(Max)) + 1):  # 对k位数排k次,每次按某一位来排
        arr = [[] for i in range(0, 10)]
        for i in ls:  # 将ls（待排数列）中每个数按某一位分类（0-9共10类）存到arr[][]二维数组（列表）中
            arr[getbit(i, k)].append(i)
        for i in range(0, 10):  # 对arr[]中每一类（一个列表）  按计数排序排好
            if len(arr[i]) > 0:
                arr[i] = CountSort(arr[i])
        j = 9
        n = len(ls)
        for i in range(0, n):  # 顺序输出arr[][]中数到ls中，即按第k位排好
            while len(arr[j]) == 0:
                j -= 1
            else:
                ls[n - 1 - i] = arr[j].pop()
    return ls

if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = RadixSort(srcArr)
    for i in resArr:
        print(i, end=' ')
