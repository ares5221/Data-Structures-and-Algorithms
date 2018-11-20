#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
#3 选择排序
'''

def select_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(0,n):
        min = i  #记录最小元素的下标
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        if min != i:  #找到最小元素进行交换
           arr[min],arr[i] = arr[i],arr[min]
    return arr

def selection_sort2(nums):
    # 思路是将最大值逐一选择到后面
    n = len(nums)
    for i in range(n - 1, 0, -1):
        max_index = i  # 记录最大值的位置
        for j in range(i):
            if nums[j] > nums[max_index]:
                max_index = j

        if max_index != i:
            nums[i], nums[max_index] = nums[max_index], nums[i]

if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = select_sort(srcArr)
    print('选择排序结果：',resArr)