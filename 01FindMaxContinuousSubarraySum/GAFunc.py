#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
贪心算法
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
    if len(list) > 0:
        result = 0
        max_sum = []
        max_sum.insert(0,0)
    else:
        result = None
    for i in range(0,len(list)):
        if max_sum[i] < 0:
            max_sum.insert(i+1,list[i])
        else:
            max_sum.insert(i+1,max_sum[i]+list[i])
        if max_sum[i+1] > result:
            result = max_sum[i+1]
    return result
if __name__ == '__main__':
    main()