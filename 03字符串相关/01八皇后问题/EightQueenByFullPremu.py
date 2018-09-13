#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
全排列解八皇后问题'2018/9/12'
"""
from copy import deepcopy
def EightQueenByFP(src, slen):
    # 后找：字符串中最后一个升序的位置i，即：S[i]<S[i+1]
    i = slen - 2
    while i >= 0 and src[i] >= src[i+1]:
        i -=1
    if i < 0:
        return False
    # 查找(小大)：S[i+1…N-1]中比S[i]大的最小值S[j]
    j = slen -1
    while src[j] <= src[i]:
        j -=1
    # 交换：S[i]，S[j]
    # swap(src, i, j)
    src[j], src[i] = src[i], src[j]
    # 翻转：S[i+1…N-1]
    Reverse(src, i+1, slen-1)
    return True

def swap(li, i, j):
    if i == j:
        return
    temp = li[j]
    li[j] = li[i]
    li[i] = temp

def Reverse(li, i, j):
    if li is None or i < 0 or j < 0 or i >= j or len(li) < j + 1:
        return
    while i < j:
        swap(li, i, j)
        i += 1
        j -= 1

if __name__ == '__main__':
    queenNum = 8
    src = [i for i in range(queenNum)]
    result = [deepcopy(src)]
    while EightQueenByFP(src, len(src)):
        result.append(deepcopy(src))
    for i in result:
        print(i)