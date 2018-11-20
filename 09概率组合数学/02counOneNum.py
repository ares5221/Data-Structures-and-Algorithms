#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
给定一个32位无符号整数N，求整数N的二进制数中1的个数。
显然：可以通过不断的将整数N右移，判断当前数字的最低位是否为1，直到整数N为0为止。
平均情况下，大约需要16次移位和16次加法。

每次最低位清0只需要n&=(n-1)即可
'''


def oneNum(n):
    return bin(n & 0xffffffff).count('1')


def oneNum2(n):
    c = 0
    while n & 0xffffffff != 0:
        n &= (n - 1)
        c += 1
    return c


if __name__ == '__main__':
    n = 167
    print(bin(n))
    print(oneNum2(n))
