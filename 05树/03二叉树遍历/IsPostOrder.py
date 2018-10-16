#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断该序列是否是二叉查找树的后序遍历 如1,2,5,4,3
由于后序遍历的最后一个元素为根结点，根据该结点，将数组分成前后两段，使得前半段都小于根结点，后半段都大于根结点；
如果不存在这样的划分，则不可能是后序遍历的结果。
递归判断前后半段是否满足同样的要求。
"""
def IsPostOrder(a, n):
    if n <=0:
        return False
    root = a[-1]
    nleft = 0 #在二叉搜索树中的左子树的节点小于根节点
    for nleft in range(0,n):
        if a[nleft] > root:
            break
    nRight = nleft #在二叉搜索树中的右子树的节点大于根节点
    for nRight in range(nleft,n):
        if a[nRight] < root:
            return False
    left = True #判断左子树是不是二叉搜索树
    if nleft > 0:
        left = IsPostOrder(a[0:nleft],nleft)
    right = True #判断右子树是不是二叉搜索树
    if nRight < n-1:
        right = IsPostOrder(a[nleft:],n- nleft-1)
    return left and right

if __name__ == '__main__':
    # post = [1,2,3,4,5]
    # post = [5,4,3,2,1]
    # post = [3,5,1,4,2]
    # post = [1,2,5,4,3]
    post = [5,6,4,10,12,7,8]
    # post = [5,6,4,10,14,12,8]
    is_postOrder = IsPostOrder(post, len(post))
    print(is_postOrder)
