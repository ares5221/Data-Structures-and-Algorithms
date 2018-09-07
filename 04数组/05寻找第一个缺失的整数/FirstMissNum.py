#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def FirstMissNumber(src):
    i, slen = 0, len(src)
    while i <= slen -1:
        if src[i] == i:
            i +=1
        elif src[i] < i or src[i] >= slen or src[i] == src[src[i]]:
            src[i] = src[slen -1]
            slen -= 1
        else:
            src[src[i]], src[i] = src[i], src[src[i]]
    return i

if __name__ == '__main__':
    src = [3, 5, 1, 2, -3, 7, 4 ,8]
    fmn = FirstMissNumber(src)
    print('第一个缺失的整数是：',fmn,src[fmn])