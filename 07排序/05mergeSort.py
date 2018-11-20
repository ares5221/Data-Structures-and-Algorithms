#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
#5 归并排序
'''

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mergeSort(arr, 0, n-1)
    return arr

#递归调用归并排序
def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right)//2
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    Merge(arr,left,mid,right)

#合并左右子序列函数
def Merge(arr, left, mid, right):
    temp = []  # 中间数组
    i = left  # 左段子序列起始
    j = mid + 1  # 右段子序列起始
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    for i in range(left, right + 1):  # !注意这里，不能直接arr=temp,他俩大小都不一定一样
        arr[i] = temp[i - left]


if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = merge_sort(srcArr)
    print('归并排序结果：',resArr)