#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#构造旋转后的数组
res =list(map (lambda x:x+2, range(10,500)))
print(res)
li1 = res[0:50]
li2 = res[-50:]
li2.extend(li1)
print(li2)
#查找最小值
def FindMinValue(numList):
    lowPoint = 0
    highPoint = len(numList)
    while lowPoint < highPoint:
        midPoint = int((lowPoint + highPoint) / 2)
        # print(numList[midPoint],'---------')
        if (numList[midPoint] < numList[lowPoint]):
            highPoint = midPoint
        else:
            lowPoint = midPoint +1
    return numList[lowPoint]

if __name__ == '__main__':
    minValue = FindMinValue(li2)
    print(minValue)
