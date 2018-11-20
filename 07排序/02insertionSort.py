#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
#2 插入排序
'''

def insert_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1,n):  #默认第一个是有序的，从第二个数开始排序比较
        key = i - 1
        mark = arr[i]  # 注： 必须将ary[i]赋值为mark，不能直接用ary[i]
        while key >= 0 and arr[key] > mark:
            arr[key + 1] = arr[key]
            key -= 1
        arr[key + 1] = mark
    return arr

if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = insert_sort(srcArr)
    print('插入排序结果：',resArr)