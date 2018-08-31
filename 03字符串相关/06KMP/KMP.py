#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KMP
"""
import random
import datetime
def KMPStringSearch(src, pat):
    slen = len(src)
    plen = len(pat)
    if slen >= plen:
        i, j = 0, 0
        # 生成KMP中所需的next数组
        next_list = [0 for i in range(plen)]
        GetNext(pat,next_list)
        while i < slen:
            if j == -1 or src[i] == pat[j]:
                i += 1
                j += 1
            else:
                j = next_list[j]
            if j == plen:
                return i - plen
    return '文本串中不存在模式串'

def GetNext(pat, next_list):
    next_list[0] = -1
    j, k = 0, -1
    while j < len(pat) -1:
        if k == -1 or pat[j] == pat[k]:
            j += 1
            k += 1
            next_list[j] = k
        else:
            k = next_list[k]
    print('The Next_List is ', next_list)

def rand_str(strLen):
    str_gen = ''
    for i in range(strLen):
        str_gen += random.choice('abcd')
    return str_gen

if __name__ == '__main__':
    src = rand_str(20)
    patten = rand_str(2)
    print("The src is : ", src)
    print("The patten is : ", patten)
    time_start = datetime.datetime.now()
    pos = KMPStringSearch(src, patten)
    print(pos)
    time_end = datetime.datetime.now()
    print("BF1 spend ", time_end - time_start)


