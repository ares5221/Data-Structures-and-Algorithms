#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A == None:
            return 1
        n = len(A)
        for i in range(n):
            digit = A[i]
            while digit>0 and digit<=n and A[digit -1] != digit:
                A[i],A[digit -1] = A[digit-1],A[i]
                digit = A[i]
        for i in range(n):
            if A[i]!= i +1:
                return i+1
        return n +1

if __name__ == '__main__':
    src = [3, 5, 1, 2, -3, 7, 4 ,8]
    ss = Solution()
    pp = ss.firstMissingPositive(src)
    print('第一个缺失的整数是：',pp)