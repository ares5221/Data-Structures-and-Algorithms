#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图的遍历
"""
class graph:
    def __init__(self,value):
        self.value=value
        self.neighbors=None

# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
from queue import Queue
def bfs(node):
    if node is None:
        return
    queue = Queue()
    nodeSet = set()
    queue.put(node)
    nodeSet.add(node)
    while not queue.empty():
        cur = queue.get()               # 弹出元素
        print(cur.value)                # 打印元素值
        for next in cur.neighbors:          # 遍历元素的邻接节点
            if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
                nodeSet.add(next)
                queue.put(next)

# 图的深度优先遍历(非递归)
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.value)
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()               # 弹出最近入栈的节点
        for next in cur.neighbors:         # 遍历该节点的邻接节点
            if next not in nodeSet:    # 如果邻接节点不重复
                stack.append(cur)       # 把节点压入
                stack.append(next)      # 把邻接节点压入
                nodeSet.add(next)           # 登记节点
                print(next.value)       # 打印节点值
                break                   # 退出，保持深度优先

def dfs1(node,nodeset):#递归深度优先遍历
    if node is None:
        return
    print(node.value)
    nodeset.add(node)
    for next in node.neighbors:
        if next not in nodeset:
            dfs1(next, nodeset)

# init graph
node5=graph(5)
node4=graph(4)
node3=graph(3)
node2=graph(2)
node1=graph(1)
nodeset=set()
node4.neighbors=[node3,node2,node1]
node3.neighbors=[node4]
node2.neighbors=[node4,node5]
node1.neighbors=[node4]
node5.neighbors=[node2]

dfs1(node4,nodeset)
dfs(node4)
bfs(node4)