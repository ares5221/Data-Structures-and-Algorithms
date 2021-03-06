#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
manacher算法
"""
def Manacher(s):
    lens = len(s)
    f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度 p
    maxj = 0  # 记录对i右边影响最大的字符位置j   id
    maxl = 0  # 记录j影响范围的右边界           mx
    maxd = 0  # 记录最长的回文子串长度
    for i in range(lens):  # 遍历字符串
        if maxl > i:
            count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
        else:
            count = 1
        while i - count >= 0 and i + count < lens and s[i - count] == s[i + count]:  # 两边扩展
            count += 1
        if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
            maxl, maxj = i - 1 + count, i
        f.append(count * 2 - 1)
        maxd = max(maxd, f[i])  # 更新回文子串最长长度
    return int((maxd + 1) / 2) - 1  # 去除特殊字符


def manacher(s: str) -> list:
    # s = '#' + '#'.join(s0) + '#'
    l = len(s)
    r = [0] * l
    mx, pos = 0, 0
    for i in range(l):
        if i > mx:
            r[i] = 1
        else:
            r[i] = min(r[2 * pos - i], mx - i)
        while i - r[i] >= 0 and i + r[i] < l and s[i + r[i]] == s[i - r[i]]:
            r[i] += 1
        if r[i] + i - 1 > mx:
            mx = r[i] + i - 1
            pos = i
    return r

if __name__ == '__main__':
    src = 'abcdzdcab'
    src = '#' + '#'.join(src) + '#'  # 字符串预处理，用特殊字符隔离字符串，方便处理偶数子串
    res = Manacher(src)
    print(src, ' 最长回文子串是：', res)

    res1 = manacher(src)
    print(src, ' 最长回文子串是：', res1)