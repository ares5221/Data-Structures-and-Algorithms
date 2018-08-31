#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串匹配之暴力破解
假设现在我们面临这样一个问题：有一个文本串S，和一个模式串P，现在要查找P在S中的位置，怎么查找呢
如果用暴力匹配的思路，并假设现在文本串S匹配到 i 位置，模式串P匹配到 j 位置，则有：
如果当前字符匹配成功（即S[i] == P[j]），则i++，j++，继续匹配下一个字符；
如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0。相当于每次匹配失败时，i 回溯，j 被置为0。
"""
import random
import datetime
def BFStringSearch(src, pat):
    i, j = 0,0
    plen = len(pat)
    slen = len(src) - plen
    while i < slen and j < plen:
        if src[i + j] == pat[j]:
            j +=1
        else:
            i +=1
            j = 0
    if j >= plen:
        print(i)
        return i
    return '文本串中不存在模式串'

def BFStringSearch2(src, pat):
    slen = len(src)
    plen = len(pat)
    i, j = 0, 0
    while i < slen and j < plen:
        if src[i] == pat[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == plen:
        return i -j
    return -1

def rand_str(strLen):
    # str = []
    str = ''
    for i in range(strLen):
        # str.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        # str += random.choice('abcdefghijklmnopqrstuvwxyz')
        str += random.choice('abcd')
    return str

if __name__ == '__main__':
    # src = 'abcdabacd'
    # patten = 'bcd'
    src = rand_str(200)
    patten = rand_str(5)
    print("The src is : ", src)
    print("The patten is : ", patten)
    time_start = datetime.datetime.now()
    pos1 = BFStringSearch(src, patten)
    print(pos1)
    time_end = datetime.datetime.now()
    print("BF1 spend ", time_end - time_start)

    time_start1 = datetime.datetime.now()
    pos2 = BFStringSearch2(src, patten)
    print(pos2)
    time_end1 = datetime.datetime.now()
    print("BF2 spend ", time_end1 - time_start1)