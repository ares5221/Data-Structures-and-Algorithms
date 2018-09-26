#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力求解
"""
def Longpalindrome(src, slen):
    if slen == 0:
        return None
    if slen == 1:
        return src
    max_length = 0
    palindromic = ''
    for i in range(slen):
        for j in range(i+1, slen):
            is_palindromic = True
            for k in range(i, int((i+j)/2)+1):
                if src[k] != src[j-k+i]:
                    is_palindromic = False
                    break
            if is_palindromic and (j-i+1) > max_length:
                max_length = j-i+1
                palindromic = src[i:j+1]
    return palindromic

if __name__ == '__main__':
    src = 'abcdzdcab'
    slen = len(src)
    res = Longpalindrome(src, slen)
    print(src,' 最长回文子串是：',res)