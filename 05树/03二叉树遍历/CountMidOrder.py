#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
已知前序后序，求中序可能出现的次数
前序遍历为ab，后序遍历为ba，此时无法确定b是为左子树还是右子树，那么就产生了一个特殊节点。当这种节点有n个时，中序遍历的可能性就有2^n
a[i]==b[j]时，a[i+1]==b[j-1]则产生一个特殊节点
"""
def CountMidOrder(pre,post):
    res,count = 0, 0
    if len(pre) == 0 or len(post) == 0:
        return
    if len(pre) == 1 or len(post) == 1:
        res = 1
    for i in range(len(pre)):
        for j in range(1, len(post)):
            if pre[i] == post[j] and pre[i+1] == post[j-1]:
                count += 1
    res = pow(2,count)
    return res
if __name__ == '__main__':
    pre = ['a', 'b', 'c']
    post = ['c', 'b', 'a']
    res = CountMidOrder(pre,post)
    print('该前序后序遍历下，中序遍历可能出现的情况个数为：',res)

    print('大整数845678992357836701转化成16进制表示，'
          '最后两位字符是',hex(845678992357836701))