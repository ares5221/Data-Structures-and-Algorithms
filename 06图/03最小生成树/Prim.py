#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prim算法
"""
def prim(graph, vertex_num):
    INF = 1 << 10
    visit = [False] * vertex_num
    dist = [INF] * vertex_num
    #preIndex = [0] * vertex_num
    #对所有的顶点进行循环，首先是确定头结点
    #找到当前无向图的最小生成树
    for i in range(vertex_num):
        minDist = INF + 1
        nextIndex = -1
        #第一次循环时，nextIndex就是头结点
        #所以要把minDIst加上1，之后这个循环
        #的功能是找到基于当前i，邻接矩阵中i行到哪一行距离最小的那个位置作为下一个结点，当然前提是那个结点没有去过
        for j in range(vertex_num):
            if dist[j] < minDist and not visit[j]:
                minDist = dist[j]
                nextIndex = j
        print (nextIndex)
        visit[nextIndex] = True
        #由于前面已经找到了下一个结点了，现在就要构建再下一个结点的dist矩阵了，这就要看当前这个nextIndex这一行了
        for j in range(vertex_num):
            if dist[j] > graph[nextIndex][j] and not visit[j]:
                dist[j] = graph[nextIndex][j]
                #preIndex[j] = nextIndex
    return dist, #preIndex

if __name__ == '__main__':
    _ = 1 << 10  # init inf
    graph = [
        [0, 6, 3, _, _, _],
        [6, 0, 2, 5, _, _],
        [3, 2, 0, 3, 4, _],
        [_, 5, 3, 0, 2, 3],
        [_, _, 4, 2, 0, 5],
        [_, _, _, 3, 5, 0],
    ]
    prim(graph, 6)