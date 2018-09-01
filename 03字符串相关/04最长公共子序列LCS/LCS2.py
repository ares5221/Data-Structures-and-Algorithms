#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
递归方法求最长公共子序列的长度
1)设有字符串a[0...n]，b[0...m]，当数组a和b对应位置字符相同时，则直接求解下一个位置；当不同时取两种情况中的较大数值。
"""
def LCS2(i, j):
    if i >= aLength or j >= bLength:
        return 0
    if aString[i] == bString[j]:
        return 1 + LCS2(i+1,j+1)
    else:
        return LCS2(i + 1, j) if LCS2(i+1,j) > LCS2(i,j+1) else LCS2(i,j+1)

if __name__ == '__main__':
    # aString = 'ABCBDAB'
    # bString = 'BDCABA'
    aString = "ABCBDAB"
    bString = "BDCABA";
    aLength = len(aString)
    bLength = len(bString)
    print('最长公共子序列长度为：', LCS2(0,0))
