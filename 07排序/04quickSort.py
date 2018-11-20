#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
#4 快速排序
'''

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    quicksort(arr, 0, n-1)
    return arr

def quicksort(arr, left, right):  # 递归调用
    if left >= right:
        return
    mid = partition(arr, left, right)
    quicksort(arr, left, mid - 1)
    quicksort(arr, mid + 1, right)

def partition(arr, left, right):
    key = left  # 划分参考数索引,默认为第一个数，可优化
    while left < right:
        while left < right and arr[right] >= arr[key]:
            right -= 1
        while left < right and arr[left] <= arr[key]:
            left += 1
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[key] = arr[key], arr[left]
    return left

'''
另外一种实现方法
先从待排序的数组中找出一个数作为基准数（取第一个数即可），然后将原来的数组划分成两部分：
小于基准数的左子数组和大于等于基准数的右子数组
。然后对这两个子数组再递归重复上述过程，直到两个子数组的所有数都分别有序。
最后返回“左子数组” + “基准数” + “右子数组”，即是最终排序好的数组。
'''
# 实现快排
def quicksort2(nums):
    if len(nums) <= 1:
        return nums
    less = []# 左子数组
    greater = [] # 右子数组
    base = nums.pop() # 基准数
    for x in nums:# 对原数组进行划分
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort2(less) + [base] + quicksort2(greater)


if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = quick_sort(srcArr)
    print('快速排序结果：',resArr)
    print('快速排序2结果：', quicksort2(srcArr))