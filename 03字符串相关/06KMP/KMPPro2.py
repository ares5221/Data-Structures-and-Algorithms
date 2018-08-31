#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/8/31'
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KMP Pro
"""
import random
import datetime
def KMPPro2(src, pat):
    slen = len(src)
    plen = len(pat)
    if slen >= plen:
        i, j = 0, 0
        # 生成KMP中所需的next数组
        next_list = [0 for i in range(plen)]
        # GetNext(pat, next_list) # 比较改进后的Next数组与原来的Next之间的差异
        GetNext3(pat,next_list)

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
    print('The Next_List1 is ', next_list)

def GetNext3(pat, next_list):
    next_list[0] = -1
    next_list[1] = 0
    for i in range(2, len(pat)):
        tmp = i - 1
        for j in range(tmp, 0, -1):
            if equals(pat, i, j):
                next_list[i] = j
                break
            next_list[i] = 0
    print('The Next_ListPro is ', next_list)

def equals(s, i, j):
    k = 0
    m = i - j
    while k <= j - 1 and m <= i - 1:
        if s[k] == s[m]:
            k = k + 1
            m = m + 1
        else:
            return False
    return True

def rand_str(strLen):
    str_gen = ''
    for i in range(strLen):
        str_gen += random.choice('abcd')
    return str_gen

if __name__ == '__main__':
    src = rand_str(20)
    patten = rand_str(3)
    print("The src is : ", src)
    print("The patten is : ", patten)
    time_start = datetime.datetime.now()
    pos = KMPPro2(src, patten)
    print(pos)
    time_end = datetime.datetime.now()
    print("BF1 spend ", time_end - time_start)


