#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力求解
"""
def TwoNumSum(src, Sum):
    if src is None or len(src) == 1:
        return None
    res = []
    for i in range(len(src)):
        for j in range(i,len(src)):
            if i != j and src[i] + src[j] == Sum:
                res.append((src[i], src[j]))
    return res

if __name__ == '__main__':
    # src = [1,3,4,6,9,2,5]
    src = [1]
    Sum = 8
    res = TwoNumSum(src, Sum)
    print(res)