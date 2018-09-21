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
    

if __name__ == '__main__':
    src = 'abcdzdcab'
    slen = len(src)
    res = Longpalindrome(src, slen)
