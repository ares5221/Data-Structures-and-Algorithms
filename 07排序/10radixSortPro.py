#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
def radixSort():
    A=[random.randint(1,9999) for i in range(100)]
    for k in range(4):  #4轮排序
        s=[[] for i in range(10)]
        for i in A:
            s[i//(10**k)%10].append(i)
        A=[a for b in s for a in b]
    return A

print(radixSort())