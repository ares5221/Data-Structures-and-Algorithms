#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
递归不包含重复
'''
def FullPermuta(src,index):
    if src is None:
        return None
    if len(src) == 1:
        return list(src)

    if index > 0 and index == len(src) -1:
        print(''.join(src))

    for i in range(index, len(src)):
        # temp = src[i]   # 传统两数交换方式
        # src[i] = src[index]
        # src[index] = temp
        src[i],src[index] = src[index], src[i]  #python的swap方法
        FullPermuta(src, index+1)
        src[i], src[index] = src[index], src[i]

if __name__ == '__main__':
    src = '1234'
    src = list(src)
    FullPermuta(src, 0)