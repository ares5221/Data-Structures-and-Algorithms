#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
字符串全排列的非递归算法 依次找最近的下一个排列值
'''
from copy import deepcopy
def GetNextPerm(src, slen):
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
    """
    翻转
    :param li: 字符串数组
    :param i: 翻转开始位置
    :param j: 翻转结束位置
    """
    if li is None or i < 0 or j < 0 or i >= j or len(li) < j + 1:
        return
    while i < j:
        swap(li, i, j)
        i += 1
        j -= 1

if __name__ == '__main__':
    src = [1,2,3,2,4,5]
    src.sort()  # 初始的src必须是正序的 [1, 2, 2, 3, 4, 5]
    result = [deepcopy(src)]
    while GetNextPerm(src, len(src)):
        result.append(deepcopy(src))
    for i in result:
        print(i)