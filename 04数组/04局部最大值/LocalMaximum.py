#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查找局部最大值
"""
def LocalMaximum(src):
    srclen = src.count()
    print(srclen)
    return srclen

if __name__ == '__name__':
    src = [2,3,6,8,12,5,6,7,9,15,32,43]
    localMax = LocalMaximum(src)
    print(src.count())