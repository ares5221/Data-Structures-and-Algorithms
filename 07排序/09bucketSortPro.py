#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def BucketSort(ls):
    #桶内使用快速排序
    def QuickSort(ls):
        def partition(arr, left, right):
            key = left  # 划分参考数索引,默认为第一个数，可优化
            while left < right:
                while left < right and arr[right] >= arr[key]:
                    right -= 1
                while left < right and arr[left] <= arr[key]:
                    left += 1
                (arr[left], arr[right]) = (arr[right], arr[left])
            (arr[left], arr[key]) = (arr[key], arr[left])
            return left

        def quicksort(arr, left, right):  # 递归调用
            if left >= right:
                return
            mid = partition(arr, left, right)
            quicksort(arr, left, mid - 1)
            quicksort(arr, mid + 1, right)

        # 主函数
        n = len(ls)
        if n <= 1:
            return ls
        quicksort(ls, 0, n - 1)
        return ls

    ######################
    n = len(ls)
    big = max(ls)
    num = big // 10 + 1
    bucket = []
    buckets = [[] for i in range(0, num)]
    for i in ls:
        buckets[i // 10].append(i)  # 划分桶
    for i in buckets:  # 桶内排序
        bucket = QuickSort(i)
    arr = []
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0, n):
        ls[i] = arr[i]
    return ls


if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = BucketSort(srcArr)
    for i in resArr:
        print(i, end=' ')
