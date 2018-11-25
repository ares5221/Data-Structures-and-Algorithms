#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
错位排列
'''
def wrongPos(n):
    if n==1:
        return 0
    if n== 2:
        return 1
    return (n-1)*(wrongPos(n-2)+wrongPos(n-1))

if __name__ == '__main__':
    for i in range(1,10):
        print(i,'的错位排序数为：',wrongPos(i))
