#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
最长递增子序列 设长度为N的数组为{a0，a1, a2, ...an-1}，则
假定以aj结尾的数组序列的最长递增子序列长度为L(j)，则L(j)={ max(L(i))+1, i<j且 a[i]<a[j] }。
也就是说，我们需要遍历在j之前的所有位置i(从0到j-1)，找出满足条件 a[i]<a[j]的L(i)，求出max(L(i))+1即为L(j)的 值。
最后，我们遍历所有的L(j)(从0到N-1)， 找出最大值即为最大递增子序列。时间复杂 度为O(N2)。
"""
def LIS(lis):
    n = len(lis)
    m = [1] * n
    for i in range(n):
        for j in range(i):
            if lis[i] > lis[j] and m[i] < m[j] +1:
                m[i] = m[j] +1
    max_value = 0
    for k in range(n):
        # print(m[k])
        if m[k] > max_value:
            max_value = m[k]
    return max_value

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("最大递增子序列长度：", LIS(arr))