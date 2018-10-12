#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
完美洗牌算法
"""
import math
# 数组下标从1开始，f是圈的头部，mod为2*n+1
def cycleLeader(a, f, mod):
    i = 2 * f % mod
    while (i != f):
        t = a[i - 1]
        a[i - 1] = a[f - 1]
        a[f - 1] = t
        # print(a[i-1],a[f-1])
        i = 2 * i % mod

def reverseString(s, f, to):
    while (f < to):
        t = s[f]
        s[f] = s[to]
        s[to] = t
        f += 1
        to -= 1
def leftRotateString(s, n, m):
    m %= n
    reverseString(s, 0, m - 1)
    reverseString(s, m, n - 1)
    reverseString(s, 0, n - 1)
    # print(''.join(s))

def perfectShuffle2(a, n):
    final = []
    while (n > 1):
        n2 = n * 2
        # step 1 找到 2*m = 3^k-1 使得 3^k <= 2*n < 3^(k+1)
        m, k = 1, 0  # 环的个数, 3的次数
        # 2*m = 3^k-1
        # m <= n  ->  2*m <= 2*n  -> 3^k-1 <= 2*n
        # 寻找最大的k使得3^k-1 <= 2*n
        while ((n2 + 1) / m >= 3):
            k += 1
            m *= 3
        m = math.floor(m / 2)
        # step 2 把a[m + 1..n + m]那部分循环右移m位 也就是循环左移n - m位
        t1 = a[:m]
        t2 = a[m:m + n]
        t3 = a[m + n:]
        leftRotateString(t2, n, n - m)
        # step 3 对每个i = 0,1,2..k-1，3^i是个圈的头部，做cycle_leader算法，数组长度为m，所以对2*m + 1取模。
        # k个环环起始位置start: 1, 3... 3^(k-1)
        i, t = 0, 1
        a = t1 + t2 + t3
        while (i < k):
            cycleLeader(a, t, m * 2 + 1)
            i += 1
            t *= 3
        # step4对数组的后面部分A[2 * m + 1..2*n]继续使用本算法, 这相当于n减小了m。
        final += a[:2 * m]
        a = a[2 * m:]
        n -= m
    if n == 1:  # 仅剩两个元素时
        t = a[0]
        a[0] = a[1]
        a[1] = t
        final += a
    print("洗牌后顺序\n",final)

if __name__ == "__main__":
    l3 = [i for i in range(1, 101)]
    # l3 = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # l3=[1,2,3,4,5,'a','b','c','d','e']
    perfectShuffle2(l3, int(len(l3) / 2))

