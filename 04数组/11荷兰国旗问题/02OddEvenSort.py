#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定整数数组，要求奇数在前，偶数在后 快排思路
"""
def OddEvenSort(src):
    begin, end = 0, len(src) -1
    while begin < end:
        if src[begin] % 2 == 0 and src[end] % 2 == 1:
            src[begin], src[end] = src[end], src[begin]
            begin +=1
            end -= 1
        else:
            if src[begin] % 2 == 1:
                begin += 1
            if src[end] % 2 == 0:
                end -= 1
    print("奇偶排序后结果",src)

if __name__ == '__main__':
    src = [i for i in range(1,20)]
    print("原数组：",src)
    OddEvenSort(src)