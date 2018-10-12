#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
位置变换
"""
def PerfectShuffle1(src):
    slen = len(src)
    if slen < 3 or slen / 2 == 1:
        return
    b = [i+1 for i in range(0, slen)]
    for i in range(1, slen):
        b[(i * 2) % (slen - 1)] = src[i]
    for j in range(1, slen):
        src[j] = b[j]
    print('PerfectShuffle 1:\n',src)

if __name__ == "__main__":
    src = [i for i in range(1,101)]
    print(src)
    PerfectShuffle1(src)