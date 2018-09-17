#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
求解一个集合的所有子集
"""
def GetSubSet1(n, src, cur):
    for i in range(cur):
        print(src[i])
    s = cur if src[cur -1] +1 else 0
    for i in range(s, n):
        src[cur] = i
        GetSubSet1(n,src,cur+1)

if __name__ == '__main__':
    src = [1,2,3,4,5]
    GetSubSet1(4,src,0)

