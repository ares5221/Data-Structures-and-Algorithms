#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力求解可以列出所有子集的情况，若和为sum则输出
在GetAllSubSet中我们讨论如何求解一个集合的所有子集
"""
def PowerSetsBinary(items):
  #二进制表示集合的所有情况1为取这个值，0为不取
  N = len(items)
  #enumerate the 2**N possible combinations
  for i in range(2**N):
    combo = []
    for j in range(N):
      if (i >> j ) % 2 == 1:
          combo.append(items[j])
    yield combo

if __name__ == '__main__':
    src = [1,2,3,4,5]
    s_sum = 10
    res = PowerSetsBinary(src)
    print('和为定值：', s_sum, '的子集如下：')
    for i in res:
        res_sum = 0
        for j in range(len(i)):
            res_sum += i[j]
        if res_sum == s_sum:
            print(i)