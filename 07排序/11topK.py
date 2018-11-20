#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# n个整数，找出其中最大的k个数
构建一个k的小顶堆T，从k+1开始，若小于T[0]，则更新该小顶堆
或者构建n的小顶堆返回末尾的k个数 及构建n的大顶堆返回前k个数
后一种时间复杂度更优，但消耗空间较大
'''

def heap_sort(ary, num):
    def siftdown(ary, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and ary[j + 1] < ary[j]:
                j += 1
            if e < ary[j]:
                break
            ary[i] = ary[j]
            i, j = j, j * 2 + 1
        ary[i] = e

    end = len(ary)
    for i in range(end // 2 - 1, -1, -1):
        siftdown(ary, ary[i], i, end)

    # 方法1
    for i in range(end - 1, -1, -1):
        e = ary[i]
        ary[i] = ary[0]
        siftdown(ary, e, 0, i)
    return ary[:-num - 1:-1]

    # 方法2
    '''
    li = []
    for i in range(num):
            if len(ary) > i:
                    li.append(ary[0])
                    e = ary[end-1-i]
                    siftdown(ary, e, 0, end-1-i)
            else:
                    break
    return li       
    '''


if __name__ == '__main__':
    a = [4, 5, 1, 6, 2, 7, 3, 8]
    num = int(input("最小的k个数:"))
    print(heap_sort(a, num))
