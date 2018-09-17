#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/9/14'
"""
def GetCantor(src, cantor, slen):
    for i in range(slen):
        for j in range(i+1,slen):
            if src[j] < src[i]:
                cantor[i] +=1
    print('原数组：',src,'其cantor数组为：',cantor)

def FromCantorToSrcPro(cantor, res):
    clen = len(cantor)
    for i in range(clen):
        for j in range(clen):
            if res[j] != 0:
                continue
            if cantor[j] == 0:
                break
            cantor[j] -=1
        res[j] = i+1
    print('cantor数组为：', cantor,'其原数组：',res)

if __name__ == '__main__':
    src = [4,6,2,5,3,1]
    slen = len(src)
    cantor = [0 for i in range(slen)]
    # 从原数组生成cantor数组
    GetCantor(src,cantor,slen)
    # 从cantor数组倒推原数组
    res = [0 for i in range(len(cantor))]
    FromCantorToSrcPro(cantor,res)