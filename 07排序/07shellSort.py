#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 希尔排序
# 双杠用于整除（向下取整），在python直接用 “/” 得到的永远是浮点数，
# 用round()得到四舍五入值
def shell_sort(nums):
    size = len(nums)
    gap = size >> 1
    while gap > 0:
        for i in range(gap, size):
            j = i
            while j >= gap and nums[j - gap] > nums[j]:
                nums[j - gap], nums[j] = nums[j], nums[j - gap]
                j -= gap
        gap = gap >> 1

if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(nums)
    print('希尔排序：', nums)
