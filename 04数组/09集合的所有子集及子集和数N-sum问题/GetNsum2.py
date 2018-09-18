#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剪枝 递归求解和为sum的数组中的数
"""
def NumforSum(src, slen, s_sum, flag, i, has):
    if i >= slen or slen == 0:
        return
    if has + src[i] == s_sum:
        flag[i] = True
        print(flag)
        flag[i] = False
    flag[i] = True
    NumforSum(src, slen, s_sum, flag, i+1, has+ src[i])
    flag[i] = False
    NumforSum(src, slen, s_sum, flag, i + 1, has)

if __name__ == '__main__':
    src = [1,2,3,4,5]
    s_sum = 10
    slen = len(src)
    flag = [False for i in range(slen)]
    cur_sum = 0
    NumforSum(src, slen, s_sum, flag, 0, cur_sum)