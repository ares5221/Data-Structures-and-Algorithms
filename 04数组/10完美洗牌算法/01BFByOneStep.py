#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
步步前移
"""
def MoveOneByOne(src):
    slen = len(src)
    if slen < 3 or slen / 2 == 1:
        return
    size = int(slen / 2)
    for i in range(size, slen-1):
        count = size - (i - size)
        index = i
        for j in range(1, count):
            src[index], src[i-j] = src[i-j], src[index]
            index = i-j
    print('步步前移后:\n',src)

if __name__ == "__main__":
    src = [i for i in range(1,101)]
    print(src)
    MoveOneByOne(src)