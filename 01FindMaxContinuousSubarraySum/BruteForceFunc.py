#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力破解 计算每一个 子数组 的和，选出最大的。时间复杂度O（n**3）
"""
def main():
    list = [[6,-3,1,-2,7,-15,1,2,2],
           [1, -2, 3, 10, -4, 7, 2, -5],
           [1, 3, 10, -4, 7, 2],
           [-2, -2, -1, -1, -2],
           [-10, -3, -2, -14, 2],
           []]
    for ls in list:
        res = maxSumofSubArray(ls)
        print('max sum of subarray is', res)

def maxSumofSubArray(list):
    n = len(list)
    max_sum = 0
    if len(list) <= 0:
        max_sum = None
    for i in range(0, n):
        for j in range(i, n):
            max = 0
            for k in range(i, j+1):
                max += list[k]
            if max > max_sum:
                max_sum = max
    return max_sum

if __name__ == '__main__':
    main()