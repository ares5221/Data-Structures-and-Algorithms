#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剪枝 递归求解和为sum的数组中的数
"""
from functools import reduce
# flag[]为最终解情况，i为考察src[i]是否加入，has表示当前的和，residue表示剩余数的全部和
def NumforSum(src, slen, s_sum, flag, i, has, residue):
    if i >= slen or slen == 0:
        return
    if has + src[i] == s_sum:
        flag[i] = True
        print(flag)
        flag[i] = False
    elif has + residue >= s_sum and has + src[i] <= s_sum:
        flag[i] = True
        NumforSum(src, slen, s_sum, flag, i + 1, has + src[i], residue - src[i])
    if has + residue - src[i] >= s_sum:
        flag[i] = False
        NumforSum(src, slen, s_sum, flag, i + 1, has, residue - src[i])

if __name__ == '__main__':
    src = [1,2,3,4,5]
    s_sum = 10
    slen = len(src)
    residue = reduce(lambda x, y: x+y, src)
    # residue = sum(src)  # 对列表求和的两种方式，不用for循环
    flag = [False for i in range(slen)]
    cur_sum = 0
    NumforSum(src, slen, s_sum, flag, 0, cur_sum, residue)