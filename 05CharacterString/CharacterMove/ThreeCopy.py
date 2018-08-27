#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
三次拷贝，需要一个新的空间做中间存储
"""
def Reverse2(src, n):
    headList = src[:n]
    src[0:len(src) - n - 1] = src[n:]
    src[len(src) - n:] = headList
    print(''.join(src))

if __name__ == '__main__':
    sBefor = 'I love three things in this world, the sun ,the moon and you. ' \
             'The sun for the day, the moon for the night, and you forever!'
    print(sBefor)
    n = 5
    li = list(sBefor)
    Reverse2(li, n)