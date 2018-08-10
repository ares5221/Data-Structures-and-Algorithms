#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分治法递归：选定一个基准，这个最大子数组有三种情况：
第一：在基准左边，那么递归寻找，第二：在基准右边，同样，直接递归查找。
第三：跨越基准，就是包括这个基准左右两边都有，那么就是左边的加上右边的。其实就是基准左侧数组的最大后缀加上基准右侧的最大前缀。（在代码中基准包括在一侧就行）。
"""
def max_child(arr, low, heigh):
    if len(arr) <= 0:
        return None
    if low == heigh:
        return arr[low]
    mid = (heigh + low) // 2
    m1 = max_child(arr, low, mid)
    m2 = max_child(arr, mid + 1, heigh)

    now_left = arr[mid]
    left = arr[mid]
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + arr[i]
        if now_left > left:
            left = now_left

    now_right = arr[mid + 1]
    right = arr[mid + 1]
    for j in range(mid + 2, heigh + 1):
        now_right = now_right + arr[j]
        if now_right > right:
            right = now_right
    m3 = left + right
    result = max(m1, m2, m3)
    return result

def main():
    list = [[6,-3,1,-2,7,-15,1,2,2],
           [1, -2, 3, 10, -4, 7, 2, -5],
           [1, 3, 10, -4, 7, 2],
           [-2, -2, -1, -1, -2],
           [-10, -3, -2, -14, 2],
           []]
    for ls in list:
        res = max_child(ls, 0, len(ls)-1)
        print('max sum of subarray is', res)
if __name__ == '__main__':
    main()