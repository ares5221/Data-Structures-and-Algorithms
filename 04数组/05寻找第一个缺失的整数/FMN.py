#!/usr/bin/env python
# -*- coding: utf-8 -*-
def first_missing_number(li):
    size = len(li)
    li.insert(0, None)  # 为了方便从1开始数，在数组前面添加None占位
    i = 1
    while i <= size:
        if li[i] < i or li[i] > size:
            li[i] = li[size]
            size -= 1
        elif li[i] > i:
            # 交换
            temp = li[i]
            li[i] = li[temp]
            li[temp] = temp
        else:
            i += 1
    return i

if __name__ == '__main__':
    li = [3, 5, 1, 2, -3, 7, 14, 8]
    result = first_missing_number(li)
    print(result)