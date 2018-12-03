#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import scrapy
import xlwt, lxml
import re, json
import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy import linalg
import math

# 链表
'''链表的部分翻转【头插法，直接翻转而不必申请新空间】
头插法：
    以head为起始节点遍历n-m次，到第i次时找到的节点插入到head的next中即可
'''
# 快排对于单链表仍然适用

'''
LCA(Lowest Common Ancestor)最近公共祖先
给定一颗树T和两个结点u和v，找出u和v的最近公共祖先
问题转化：在有父指针的前提下，该问题即为寻找两个单向链表的第一个公共节点，即单链公共节点问题
如果两个单链表有公共结点，即从某一结点开始，它们的next指针都指向同一个结点
【由于单链表的结点只有一个next指针，所以从第一个公共结点开始都是重合的，不可能再出现分叉】Y型
因此，可首先遍历两个单链表l1，l2，得其长度分别为m，n（假设m>=n）
则可先将l1单链表遍历m-n次，然后同步遍历两个链表直到找到相同的结点或者链表结束
'''
# 对于没有父指针的情况下，可以通过从根到u，v的递归查找
class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.height = None
        self.freq = None

    def getLCA(self, root, node1, node2):
        if root is None:
            return None
        if root == node1 or root == node2:
            return root
        left = self.getLCA(root.lchild, node1, node2)
        right = self.getLCA(root.rchild, node1, node2)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None
'''
Tarjan算法是由Robert Tarjan在1979年发现的一种高效的离线算法，也就是说，它要首先
读入所有的询问（求一次LCA叫做一次询问），然后并不一定按照原来的顺序处理这些询问，
该算法的时间复杂度O(N*α(N)+Q)，其中，α(x)不大于4，N表示问题规模，Q表示询问次数。

Tarjan算法基于深度优先搜索，对于新搜索到的一个结点u，首
先创建由这个结点u构成的集合setU，再对当前结点u的每一个
子树subTree进行搜索，每搜索完一棵子树sub，则可确定子树
sub内的LCA询问都已解决。其他的LCA询问的结果必然在这个
子树sub之外，这时把子树sub所形成的集合setSub与当前结点的
集合setU合并成set，并将当前结点u设为这个集合set的祖先
Ua。之后继续搜索下一棵子树subNext，直到当前结点u的所有
子树搜索完。这时把当前结点u设为checked，同时可以处理有
关当前结点u的LCA询问，如果有一个从当前结点u到结点v的询
问，且v已被检查过，则由于进行的是深度优先搜索，当前结点
u与v的最近公共祖先LCA一定是未checked，而这个最近公共祖
先LCA包含v的子树subV一定已经搜索过了，那么LCA一定是v
所在集合的祖先Va。
'''


# 括号匹配

def isMatch(str):
    l = ['(', '[', '{']
    r = [')', ']', '}']
    stack = []
    length = len(str)
    if str and length % 2 == 0:
        if str[0] in r:
            return
        else:
            for i in range(0, length):
                if str[i] in l:
                    stack.append(str[i])
                else:
                    if str[i + 1] in l or r.index(str[i]) != l.index(stack[-1]):
                        print('gg', stack)
                        return
                    else:
                        stack.pop()
            if len(stack) == 0:
                print('666666')
    else:
        print(stack)
        print('gggg')


# isMatch('(({}){')

# 最长括号匹配

def longestStrMatch(str):
    length = len(str)
    stack = []
    last = -1  # 记录最深一个左括号的(前一个)位置
    c = 0
    if length == 0:
        return
    d = 0
    for i in range(0, length):
        if str[i] == '(':
            stack.append(i)
        else:
            if stack == []:
                last = i
            else:
                x = stack.pop()
                if stack == []:
                    d = max(d, i - last)
                else:
                    if x == i - 1:
                        c += 1
                        d = max(d, c * 2)
                    else:
                        d = max(d, i - x + 1)
            print(last)

    print(c, d)
    return d


# longestStrMatch('()(()())((')
# 顺序扫描，然后逆序扫描，可达到时间复杂度O(n),空间复杂度O(1)
'''
分析知,只有在右括号和左括号发生匹配时,才有可能更新最终解
做记录前缀串p[0...i-1]中左括号数目与右括号数目的差 X,若x=0,考察是否最终解得以更新即可.这个差x,其实是入栈的数目,代码中用deep表达
由于可能出现左右括号不相等,所以,再从右向前扫描一次
用deep替换了栈,空间复杂度由O(N)降到O(1)
'''


def longestStrMatch2(a):
    size = len(a)
    d = 0
    deep = 0
    start = -1  # 最深的(deep=0时)左括号的位置//其实为了方便计算长度,该变量是最深左括号的前一个位置
    for i in range(0, size):
        if a[i] == '(':
            deep += 1
        else:
            deep -= 1
            if deep == 0:
                d = max(d, i - start)
            elif deep < 0:
                deep = 0
                start = i
    deep = 0
    start = size  # 最深的右括号的位置
    for i in range(0, size, -1):
        if a[i] == ')':
            deep += 1
        else:
            deep -= 1
            if deep == 0:
                d = max(d, start - i)
            elif deep < 0:
                deep = 0
                start = i
    print(d)
    return d


longestStrMatch2('()(()())((')

# 逆波兰表达式[后缀表达式]
# 中缀表达式--二叉树，对其 后序遍历，即得逆波兰表达式【为何无需知道其先序遍历？---操作符有优先级】
# 若当前字符是操作数，则压栈
# 若当前字符是操作符，则弹出栈中的两个操作数，计算后仍压入栈中
# 若某次操作，栈内无法弹出两个操作数，则表达式有误

'''
#直方图矩形面积最大问题
给定n个非负整数，表示直方图的方柱的高度，同时，每个方柱的宽度假定都为1，求最大的矩形面积
算法思想：
    从前向后遍历a[0...size](末尾添加0)，若a[i]>a[i-1]，则a[i]入栈
    若a[i]<=a[i-1],则计算栈中能够得到的最大矩形面积
    从a[i]>a[i-1]可以得出：
        栈中放入元素递增
        每次只弹出栈顶元素和a[i]比较
显然，为了方便的计算‘横向距离’，压入栈的是方柱的索引，而非方柱的高度本身
    因为每个方柱最多只计算一次——只有压栈的方柱才会计算面积，并且每次计算一次即可完成。所以时间复杂度O(N)
'''


def largestRectangleArea(a):
    a.append(0)
    area = 0
    temp = 0
    stack = [-1]
    t = 0
    # print(stack[-1])
    if a:
        i = 0
        while i < len(a):
            # print(i)
            if a[i] > a[stack[-1]] or stack == [-1]:
                stack.append(i)
                i += 1
            else:
                print(stack)
                temp = stack.pop()
                if stack == [-1]:
                    t = i
                else:
                    t = i - stack[-1] - 1
                area = max(area, a[temp] * t)
                # print(area)
        print(area)
        return area


# largestRectangleArea([2,7,5,6,4])

# 直方图例题：收集雨水问题
# 给定n个非负整数，表示直方图的方柱的高度，同时，每个方柱的宽度假定都为1。若用其收集雨水，可以盛多少水量
# 如输入[0,1,0,2,1,0,1,3,2,1,2,1];返回6
'''
思路分析:
    记最终盛水量为trap,初值为0
    考察直方图最左边L和最右边R的两个方柱
        它们两个本身,一定不可能存储雨水:因为在最边界;
        记它们比较低的那个为X,与X相邻的方柱记作Y
            若Y>=X,可将X丢弃,且trap值不变
            若Y<X,则X-Y即为方柱Y最多盛水量;仍然丢弃X,且trap+=(X-Y)
            无论如何,L或者R都将向中间靠近一步,重复上述过程,直至L==R

'''


def collectRain(a):
    height2 = 0  # 记录第二高的方柱值
    n = len(a)
    trap, left, right = 0, 0, n - 1  # trap即盛水量
    while left < right:
        if a[left] < a[right]:
            height2 = max(a[left], height2)
            # print(height2)
            print(trap)
            trap += (height2 - a[left])
            left += 1
        else:
            height2 = max(a[right], height2)
            # print(height2)
            trap += (height2 - a[right])
            # print(trap)
            right -= 1
    print(trap)
    return trap

# collectRain([1,2,3])
