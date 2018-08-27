#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力移位 每次循环左移一位，调用k次 o(kN) 0(1)
"""
def LeftShiftOneChar(src):
    start = src[0]
    for i in range(1, len(src)):
        src[i-1] = src[i]
    src[len(src) - 1] = start

def Reverse1(src, n):
    for i in range(n):
        LeftShiftOneChar(src)
    print(''.join(src))

if __name__ == '__main__':
    sBefor = 'I love three things in this world, the sun ,the moon and you. ' \
             'The sun for the day, the moon for the night, and you forever!'
    print(sBefor)
    n = 12
    li = list(sBefor)
    Reverse1(li, n)