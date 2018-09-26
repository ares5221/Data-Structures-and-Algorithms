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
    

if __name__ == '__main__':
    src = 'abcdzdcab'
    slen = len(src)
    res = Longpalindrome2(src, slen)
    print(src,' 最长回文子串是：',res)