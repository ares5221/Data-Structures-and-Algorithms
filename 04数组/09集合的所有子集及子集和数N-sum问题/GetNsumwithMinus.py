#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数组中包含负数的剪枝求解和为sum的N个数
"""
from functools import reduce
# flag[]为最终解情况，i为考察src[i]是否加入，has表示当前的和，residue表示剩余数的全部和
def NumforSum2(src, slen, s_sum, flag, i, has, negative, positive):
    if i >= slen or slen == 0:
        return
    if has + src[i] == s_sum:
        flag[i] = True
        print(flag)
        flag[i] = False
    if src[i] >= 0:
        if has + positive >= s_sum and has + src[i] <= s_sum:
            flag[i] = True
            NumforSum2(src, slen, s_sum, flag, i + 1, has + src[i], negative, positive - src[i])
            flag[i] = False
        if has + positive - src[i] >= s_sum:
            flag[i] = False
            NumforSum2(src, slen, s_sum, flag, i+1, has, negative, positive - src[i])
    else:
        if has + src[i] + positive >= s_sum:
            flag[i] = True
            NumforSum2(src, slen, s_sum, flag, i + 1, has + src[i], negative - src[i], positive)
            flag[i] = False
        if has + positive >= s_sum and has + negative <= s_sum:
            flag[i] = False
            NumforSum2(src, slen, s_sum, flag, i + 1, has, negative - src[i], positive)

# 负数在前，正数在后排序
def sortByPos(src):
    size = len(src) -1
    if size < 0:
        return
    head, end = 0, size
    while (head < end):
        if src[head] >= 0 : # and src[end] >= 0:
            if src[end] >= 0:
                end -= 1
            else:
                src[head], src[end] = src[end], src[head]
        if src[head] < 0 : # and src[end] >= 0:
            head +=1
        # if src[head] >= 0 and src[end] < 0:
        #     src[head],src[end] = src[end],src[head]
        # if src[head] < 0 and src[end] < 0:
        #     head +=1
    return src, head  # head为正负数交界处，返回便于后面计算各自正负数的和

if __name__ == '__main__':
    src = [4, 1, -3, -5, -2, 2, 3]
    s_sum = 5
    slen = len(src)
    # 先对数组排序，负的放前面
    src,k = sortByPos(src)
    negative = reduce(lambda x, y: x+y, src[:k])
    positive = sum(src[k:])
    flag = [False for i in range(slen)]
    cur_sum = 0
    NumforSum2(src, slen, s_sum, flag, 0, cur_sum, negative, positive)