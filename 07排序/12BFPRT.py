#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from math import ceil
import copy

''' 
算法: BFPRT
作用: 给定无序浮点list，选取最大n个数
输入: ctr_scores,N个数浮点无序数组
输出: largest_n_id,n个最大数的index
时间复杂度: O(N)
空间复杂度: O(N)
example1:
    array = [6,2,3,4,1]
    print(topN(array,3)) 
    print(topN(array,1)) 
    print(topN(array,0))
    print(topN(array,5))

    [0, 2, 3]
    [0]
    []
    [0, 1, 2, 3, 4]

example2:
    array = [2,2,3,3]
    print(topN(array,3)) 
    print(topN(array,1)) 
    print(topN(array,0))
    print(topN(array,6))
    print(topN(array,2))

    [2, 3, 0]
    [2]
    []
    n should <length of ctr_scores!
    None
    [2, 3]

example3:
    array = [3,3,3,3]
    print(topN(array,3)) 
    print(topN(array,1)) 
    print(topN(array,2))

    [0, 1, 2]
    [0]
    [0, 1]
'''


# 将输入的数组划分为5个一组，不足5的单独一组，并在每个组内插入排序
def split_insertSort(array, group_num):
    for k in range(group_num):
        start = k * 5  # 需排序的子数组起点
        end = min((k + 1) * 5, len(array))  # 需排序的子数组终点
        for i in range(start + 1, end):
            if array[i - 1] > array[i]:
                temp = array[i]  # 当前需要排序的元素
                index = i  # 用来记录排序元素需要插入的位置
                while index > start and array[index - 1] > temp:
                    array[index] = array[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                    index -= 1
                array[index] = temp  # 把需要排序的元素，插入到指定位置
    return array


# 返回中位数数组
def getMedian(array, group_num):
    mArray = []

    for k in range(group_num):
        start = k * 5  # 子数组起点
        end = min((k + 1) * 5, len(array))  # 子数组终点

        if (end - start) % 2 == 1:  # 如果子数组长度奇数
            mArray.append(array[int((start + end - 1) / 2)])
        else:  # 偶数,取下中位数
            mArray.append(array[int(((start + end - 1) - 1) / 2)])
    return mArray


# 大于等于中位数的放在右边，小于中位数的放在左边
def partition(ctr_scores, median):
    left_median = []
    right_median = []

    isFirstShow = 0

    for num in ctr_scores:

        if num < median:  # 左边，小于
            left_median.append(num)

        elif num == median:  # 第一次出现忽略过去
            if isFirstShow == 0:
                isFirstShow = 1
            else:
                right_median.append(num)

        else:  # 右边，大于等于
            right_median.append(num)

    return left_median, right_median


def topN(ctr_scores, n):
    def BFPRT_findMedian(array):

        # 得到有多少组
        group_num = ceil(len(array) / 5)

        # 按照5组一个划分，并且组内插排
        array = split_insertSort(array, group_num)

        array = getMedian(array, group_num)  # O(N)

        if len(array) == 1:  # 如果已经找到，就退出递归
            return array[0]
        else:  # 递归调用求中位数
            return BFPRT_findMedian(array)

    def BFPRT_Main(ctr_scores, n):

        median = BFPRT_findMedian(ctr_scores)

        # 根据求得的中位数遍历一次，划分，小的在左边，大的在左边
        left_median, right_median = partition(ctr_scores, median)

        if len(right_median) == n:
            return median
        elif len(right_median) < n:
            left_median.append(median)
            return BFPRT_Main(left_median, n - len(right_median))
        else:

            return BFPRT_Main(right_median, n)

    ctr_scores_run = copy.copy(ctr_scores)

    if n > len(ctr_scores):
        print('n should <length of ctr_scores!')
        return

    if n == len(ctr_scores):
        median = -1
    elif n == 0:
        median = 9999999999
    else:
        median = BFPRT_Main(ctr_scores_run, n)

    largest_n_index = []
    isFirstShow = 0
    for i in range(len(ctr_scores)):  # O(N)
        if ctr_scores[i] <= median:  # 左边，小于
            continue
        else:  # 右边，大于等于
            largest_n_index.append(i)

    n -= len(largest_n_index)
    if 0 < n:  # O(N)
        for i in range(len(ctr_scores)):
            if ctr_scores[i] == median:  # 左边，小于
                largest_n_index.append(i)
                n -= 1
                if n == 0:
                    break

    return largest_n_index

if __name__ == '__main__':
    array = [6,2,3,4,1]
    print(topN(array,3))