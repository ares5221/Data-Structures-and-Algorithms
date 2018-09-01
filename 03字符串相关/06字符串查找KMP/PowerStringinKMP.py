#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KMP求解最小循环子串
需要计算到next_list[len(pStr)],因此需要在最后多补一位
"""
def Get_Next(pStr, next_list):
    if len(pStr) == 0:
        return -1
    next_list[0] = -1
    j, k = 0, -1
    while j < len(pStr) - 1:
        if k == -1 or pStr[j] == pStr[k]:
            j +=1
            k +=1
            next_list[j] = k
        else:
            k = next_list[k]
    print('Next_list is :', next_list)

if __name__ == '__main__':
    powerStr = 'abcabcabc'
    pslen = len(powerStr)
    powerStr += '\0'  # ASCII码为0，表示一个字符串结束的标志。这是转义字符。
    print('powerstring : ', list(powerStr))
    next_list = [0 for i in range(pslen +1)]
    Get_Next(powerStr, next_list)
    ans = -1
    if next_list[pslen] == 0:
        ans = -1
    else:
        if pslen % (pslen - next_list[pslen]) == 0:
            ans = pslen - next_list[pslen]
    print("最小循环子串长度为：", ans);