#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
递归包含重复字符的情况
每个字符分别与他后面的非重复出现的字符交换
'''

def IsDupllcate(src, n, t):
    while n < t:
        if src[n] == src[t]:
            return False
        n += 1
    return True

def FullPermuta(src,index):
    if src is None:
        return None
    if len(src) == 1:
        return list(src)

    if index > 0 and index == len(src) -1:
        print(''.join(src))

    for i in range(index, len(src)):
        if IsDupllcate(src, index, i):
            src[i], src[index] = src[index], src[i]  # python的swap方法
            FullPermuta(src, index + 1)
            src[i], src[index] = src[index], src[i]

if __name__ == '__main__':
    src = '1223'
    src = list(src)
    FullPermuta(src, 0)