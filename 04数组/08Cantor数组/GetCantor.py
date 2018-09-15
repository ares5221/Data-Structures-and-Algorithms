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

def FromCantorToSrc(cantor, res):
    clen = len(cantor)
    b = [i+1 for i in range(clen)]
    for i in range(clen):
        res[i] = b[cantor[i]]
        b.remove(res[i])
    print('cantor数组为：', cantor,'其原数组：',res)

if __name__ == '__main__':
    src = [4,6,2,5,3,1]
    slen = len(src)
    cantor = [0 for i in range(slen)]
    # 从原数组生成cantor数组
    GetCantor(src,cantor,slen)
    # 从cantor数组倒推原数组
    res = [0 for i in range(len(cantor))]
    FromCantorToSrc(cantor,res)