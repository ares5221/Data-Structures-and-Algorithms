#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断该序列是否是二叉查找树的后序遍历 如1,2,5,4,3
由于后序遍历的最后一个元素为根结点，根据该结点，将数组分成前后两段，使得前半段都小于根结点，后半段都大于根结点；
如果不存在这样的划分，则不可能是后序遍历的结果。
递归判断前后半段是否满足同样的要求。
"""
def IsPostOrder(a, n):
    if n <=1:
        return True
    root = a[-1]
    nleft = 0
    while nleft < n-1:
        if a[nleft] > root:
            break
        nleft +=1
    nRight = n-2 #n-1 is root
    while nRight >=0:
        if a[nRight] < root:
            break
        nRight -=1
    if nRight != nleft-1:
        return False
    return IsPostOrder(a,nleft) and IsPostOrder(a+nleft,n-nleft-1)
if __name__ == '__main__':
    post = [1,2,5,4,3]
    is_postOrder = IsPostOrder(post, len(post))
    print(is_postOrder)
