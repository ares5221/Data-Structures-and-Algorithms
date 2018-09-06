#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查找局部最大值
"""
def LocalMaximum(src):
    srclen = len(src)
    left, right = 0, len(src) -1
    while(left < right):
        mid = int((left + right) / 2)
        if src[mid] > src[mid +1]:
            right = mid
        else:
            left = mid +1
    return src[left]

if __name__ == '__main__':
    src = [2, 3, 6, 8, 12, 5, 6, 7, 9, 15, 32, 18]
    localMax = LocalMaximum(src)
    print('找到的局部最大值之一是：', localMax)