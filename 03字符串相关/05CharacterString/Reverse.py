#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
三次翻转
"""
def ReverseString(src, start, end):
    if src is None or start < 0 or end < 0 or start >= end or len(src) < end +1:
        return
    while start < end:
        t = src[start]
        src[start] = src[end]
        src[end] = t
        start += 1
        end -= 1

def Reverse3(src, n):
    if src is None:
        return
    if len(src) < n:
        return
    ReverseString(src, 0, n-1)
    ReverseString(src, n, len(src)-1)
    ReverseString(src, 0, len(src)-1)
    print(''.join(src))

if __name__ == '__main__':
    sBefor = 'I love three things in this world, the sun ,the moon and you. ' \
             'The sun for the day, the moon for the night, and you forever!'
    print(sBefor)
    n = 15
    li = list(sBefor)
    Reverse3(li, n)