#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
荷兰国旗问题 快排思路
"""
def Holland(src, n):
    begin, curr, end = 0, 0, n-1
    while curr <= end:
        if src[curr] == 2:
            src[curr], src[end] = src[end], src[curr]
            end -= 1
        elif src[curr] == 1:
            curr += 1
        else: # src[curr] == 0
            if begin == curr:
                begin += 1
                curr += 1
            else:
                src[begin], src[curr] = src[curr], src[begin]
                begin += 1
    print("排序后结果",src)

def Holland2(src, n):
    begin, curr, end = 0, 0, n-1
    while curr <= end:
        if src[curr] == 2:
            src[curr], src[end] = src[end], src[curr]
            end -= 1
        elif src[curr] == 1:
            curr += 1
        else: # src[curr] == 0
            if begin != curr:
                src[begin], src[curr] = src[curr], src[begin]
            begin += 1
            curr += 1 # 优化的地方
    print("优化后结果",src)

if __name__ == '__main__':
    src = [2, 0, 2, 0, 0, 2, 1, 1, 0, 2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 2, 1,0]
    Holland(src, len(src))
    Holland2(src, len(src))