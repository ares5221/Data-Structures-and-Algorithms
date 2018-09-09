#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
通过空间换时间，开辟一个列表存储字符是否已经存在，对于存在的字符不进行交换操作
'''

def FPermutation(src, slen, n):
    if src is None:
        return None
    if len(src) == 1:
        return src

    dup = [0 for i in range(256)]
    if n > 0 and n == len(src) -1:
        print(''.join(src))

    for j in range(n, slen):
        if dup[ord(src[j])] == 1:
            continue
        dup[ord(src[j])] = 1
        src[j], src[n] = src[n], src[j]  # python的swap方法
        FPermutation(src,len(src), n + 1)
        src[j], src[n] = src[n], src[j]

if __name__ == '__main__':
    src = 'abbc'
    src = list(src)
    FPermutation(src, len(src), 0)