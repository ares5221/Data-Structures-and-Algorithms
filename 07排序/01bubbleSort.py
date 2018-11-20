#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
#1 冒泡排序
'''

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#优化1：
#某一趟遍历如果没有数据交换，说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = True  # 标记
        for j in range(1, n - i):
            if ary[j] < ary[j - 1]:
                ary[j], ary[j - 1] = ary[j - 1], ary[j]
                flag = False
        # 某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了
        if flag:
            break
    return ary

#优化2：
#记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n  # k为循环的范围，初始值n
    for i in range(n):
        flag = True
        for j in range(1, k):  # 只遍历到最后交换的位置即可
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
                k = j  # 记录最后交换的位置
                flag = False
        if flag:
            break
    return ary


if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = bubble_sort(srcArr)
    print('冒泡排序结果：',resArr)