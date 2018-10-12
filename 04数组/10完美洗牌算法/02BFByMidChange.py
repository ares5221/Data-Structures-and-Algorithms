#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
中间交换
"""
def MidChange(src):
    slen = len(src)
    if slen < 3 or slen / 2 == 1:
        return
    size = int(slen / 2)
    count = 1
    for i in range(size, 1, -1):
        for j in range(size - count, size + count, 2):
            src[j], src[j + 1] = src[j + 1], src[j]
        count += 1
    print('步步前移后:\n',src)

if __name__ == "__main__":
    src = [i for i in range(1,101)]
    print(src)
    MidChange(src)