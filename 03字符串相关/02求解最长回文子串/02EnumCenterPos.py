#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
枚举中心位置
"""
def Longpalindrome2(src, slen):
    if slen == 0:
        return None
    if slen == 1:
        return src
    max_length = 0
    palindromic = ''
    for i in range(slen):
        x = 1  # 回文串长度为奇数
        while (i - x) >= 0 and (i + x) < slen:
            if src[i + x] == src[i - x]:
                x += 1
            else:
                break
        x -= 1
        if 2 * x + 1 > max_length:
            max_length = 2 * x + 1
            palindromic = src[i - x:i + x + 1]
        x = 0  # 回文串长度为偶数
        if (i + 1) < slen:
            while (i - x) >= 0 and (i + 1 + x) < slen:
                if src[i + 1 + x] == src[i - x]:
                    x += 1
                else:
                    break
        x -= 1
        if 2 * x + 2 > max_length:
            max_length = 2 * x + 2
            palindromic = src[i - x:i + x + 2]
    return palindromic

if __name__ == '__main__':
    src = 'abcdzdcab'
    slen = len(src)
    res = Longpalindrome2(src, slen)
    print(src, ' 最长回文子串是：', res)
