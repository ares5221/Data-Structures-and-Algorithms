#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
给定非负整数数组，初始时在数组起始位置放置一机器人，数组的每个元素表示在当前
位置机器人最大能够跳跃的数目。它的目的是用最少的步数到达数组末端。例如：给定
数组A=[2,3,1,1,2]，最少跳步数目是2，对应的跳法是：232。
不能简单使用贪心。
初始步数step赋值为0；
记当前步的控制范围是[i,j]，则用k遍历i到j
计算A[k]+k的最大值，记做j2；
step++；继续遍历[j+1,j2]
'''


def Jump(a, n):
    if n == 1:
        return 0
    step, i, j = 0, 0, 0
    while j < n:
        step += 1
        j2 = j
        for k in range(i, j + 1):
            j2 = max(j2, k + a[k])
            if j2 >= n - 1:
                return step
        i = j + 1
        j = j2
        if j < i:
            return -1
    return step


if __name__ == '__main__':
    sa = [2, 3, 1, 1, 2, 4, 1, 1, 6, 1, 7]
    res = Jump(sa, len(sa))
    print('最小步数', res)
