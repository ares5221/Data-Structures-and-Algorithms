#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dijkstra算法实现，有向图和源点作为函数的输入，(源点到图中其余点的)最短路径最为输出
"""
def dijkstra(graph,src):
    if graph is None:
        return None  # 判断图是否为空，如果为空直接退出
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited = []  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i] = graph[src][i]  # 初始化
    path = {src: {src: []}}  # 记录源节点到每个节点的路径
    k = pre = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v] + graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance  # 进行距离更新
                    k = d
                    pre = v
        distance[k] = mid_distance  # 最短路径
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        print(visited, nodes)  # 输出节点的添加过程
    return distance, path
if __name__ == '__main__':
    # graph_list = [[0, 2, 1, 4, 5, 1],
    #               [1, 0, 4, 2, 3, 4],
    #               [2, 1, 0, 1, 2, 4],
    #               [3, 5, 2, 0, 3, 3],
    #               [2, 4, 3, 4, 0, 1],
    #               [3, 4, 7, 3, 1, 0]]
    graph_list = [[0, 20, 50, 30, 999, 999, 999],
                  [999, 0, 25, 999, 999, 70, 999],
                  [999, 999, 0, 40, 25, 50, 999],
                  [999, 999, 999, 0, 55, 999, 999],
                  [999, 999, 999, 999, 0, 10, 70],
                  [999, 999, 999, 999, 999, 0, 50],
                  [999, 999, 999, 999, 999, 999, 0]]
    distance, path = dijkstra(graph_list, 0)  # 查找从源点0开始带其他节点的最短路径
    print('源点到图中各点的距离：',distance,'\n源点到图中各点最短路径为：',path)