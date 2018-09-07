#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力求解一一比较
"""
class Solution:
    def firstMissingPositive(self, A):
        flag = 1
        for i in range(1, len(A)):
            for j in range(len(A)):
                flag = 0
                if A[j] == i:
                    flag = 1
                    break
            if flag == 0:
                break
        return i

if __name__ == '__main__':
    src = [3, 5, 1, 2, -3, 7, 4 ,8]
    ss = Solution()
    pp = ss.firstMissingPositive(src)
    print('第一个缺失的整数是：',pp)


