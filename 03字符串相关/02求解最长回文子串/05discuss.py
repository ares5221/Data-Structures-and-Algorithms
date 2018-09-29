#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/9/29'
"""
def Longpalindrome4(s):
    lenS = len(s)
    if lenS <= 1: return s
    minStart, maxLen, i = 0, 1, 0
    while i < lenS:
        if lenS - i <= maxLen / 2: break
        j, k = i, i
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1
        i = k + 1
        while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
        if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
    return s[minStart: minStart + maxLen]

if __name__ == '__main__':
    src = 'abcdzdcab'
    res = Longpalindrome4(src)
    print(src, ' 最长回文子串是：', res)