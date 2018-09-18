#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
求解一个集合的所有子集
"""
def PowerSetsRecursive1(items):
    """Use recursive call to return all subsets of items, include empty set"""
    if len(items) == 0:
        return [[]]
    subsets = []
    first_elt = items[0]  # first element
    rest_list = items[1:]
    # Strategy:不断在已有子集的基础上不断增加新元素一直到无法继续增加时为止
    for partial_sebset in PowerSetsRecursive1(rest_list):
        subsets.append(partial_sebset)
        next_subset = partial_sebset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

def PowerSetsRecursive2(items):
  # 相当于使用了两个for循环
  result = [[]]
  for x in items:
    result.extend([subset + [x] for subset in result])
  return result

def PowerSetsBinary(items):
  #二进制表示集合的所有情况1为取这个值，0为不取
  N = len(items)
  #enumerate the 2**N possible combinations
  for i in range(2**N):
    combo = []
    for j in range(N):
      #test jth bit of integer i
      if(i >> j ) % 2 == 1:
        combo.append(items[j])
    yield combo

if __name__ == '__main__':
    src = [1,2,3,4,5]
    count = 0
    res = PowerSetsRecursive1(src)
    # 方法二
    res1 = PowerSetsRecursive2(src)
    res2 = PowerSetsBinary(src)
    for i in res2:
        count +=1
        print(i)
    print('集合：', src, '的全部子集个数为：', count)

# 判断b是否是a的子集
a = [1,2,3,4]
b = set([1,2])
b.issubset(a)
