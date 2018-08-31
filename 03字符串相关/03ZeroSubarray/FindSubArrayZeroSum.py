#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''求对于长度为N的数组A，求子数组的和接近0的子数组，要求时间复杂度O(NlogN) '''
'''
思路：
设定一个长度为N+1的数组sum[0,...,N]，sum[i] = A[0] + ... + A[i-1]，即，sum[i]是A的前i-1项和
则有如下性质：A[i] +...+ A[j] = sum[j+1] - sum[i]
那么求得sum数组后对sum数组排序，然后计算sum数组中相邻元素之差的绝对值的最小最min1及sum数组中的最小值min2，
其中最小的值就是A中子数组和最接近0的值。
'''
def FindSubarray(numlist):
    # 求出所有的sum[i] sum[i]表示A的前i项和
    sumList = []
    for i in numList:
        sumList.append(0)
    print('numList----->',numList)
    for i in range(len(numList)):
        if i == 0:
            sumList[0] = numList[0]
        else:
            sumList[i] = sumList[i-1] + numList[i]
    print('sumList----->',sumList)
    # 对sum排序，求相邻之差最小
    sortList = sorted(sumList)
    print('sortList--->', sortList)
    # 计算相邻元素差值，其中最小值记为min1
    min1 = sortList[1] - sortList[0]
    minofSort = []
    for j in range(1, len(sortList)):
        smin = abs(sortList[j] - sortList[j - 1])
        minofSort.append(smin)
        if abs(smin) <= abs(min1):
            min1 = abs(smin)
   # sum中最小的值为min2
    min2 = sumList[0]
    for h in sumList:
        if abs(h) < abs(min2):
            min2 = abs(h)
# 返回min1 min2中较小值
    if min1 < min2:
        for k in range(len(minofSort)):
            if minofSort[k] == min1:
                index = k + 1
                headofSubarray = sortList[index -1]
                endofSubarray = sortList[index]
                # 当和数组中存在相同值的时候导致排序后两个值相等，需要遍历获取索引，index方法只能得到找到的第一个元素
                if headofSubarray == endofSubarray:
                    # 获取到第一个索引后将该值置为None，不影响下一次寻找索引，得到end后恢复sumList列表
                    head = sumList.index(headofSubarray)
                    sumList[head] = None
                    # print(head,sumList)
                    end = sumList.index(endofSubarray)
                    sumList[head] = endofSubarray
                else:
                    head = sumList.index(headofSubarray)
                    end = sumList.index(endofSubarray)

                if head > end:
                    head ,end = end ,head
                fo = int(head) +1
                to = int(end) +1
                print('所求和最接近零的子数组1为',numList[fo:to])
        print('以上子数组和最接近0的数组和为:', min1)

    elif min2 < min1:
        otherSubarray = int(sumList.index(min2)) + 1
        print('所求和最接近零的子数组2为', numList[:otherSubarray])
        print('以上子数组和最接近0的数组和为:', min2)
    else:
        for k in range(len(minofSort)):
            if minofSort[k] == min1:
                index = k + 1
                headofSubarray = sortList[index -1]
                endofSubarray = sortList[index]
                head = sumList.index(headofSubarray)
                end = sumList.index(endofSubarray)
                if head > end:
                    head ,end = end ,head
                fo = int(head) +1
                to = int(end) +1
                print('所求和最接近零的子数组1为',numList[fo:to])
        otherSubarray = int(sumList.index(min1)) +1
        print('所求和最接近零的子数组2为',numList[:otherSubarray])
        print('以上子数组和最接近0的数组和为:',min1)

if __name__ == '__main__':
    num = [[-13, 7, -14, 15, -6, 17, 10, -11, -4],
           [-13, 12, -1, 2, -6, 17, 10, -11, -4],
           [5, 7, -14, 15, -16, 1, 10, -11, -4]
           ]
    for numList in num:
        FindSubarray(numList)
        print('------------------------------------')

