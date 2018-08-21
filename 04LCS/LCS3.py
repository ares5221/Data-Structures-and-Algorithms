#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
寻找三个字符串的最长公共子串
"""
def max1(m, n):
    return m if m > n else n

def max2(x, y, z, k, m, n):
    max = -1
    tmp = [x,y, z, k, m, n]
    return max if max > sorted(tmp)[len(tmp)-1] else sorted(tmp)[len(tmp)-1]

def GetMLCSLength(str1, str2, str3):
    # length1,length2,length3 = 3,3,2
    length1, length2, length3 = len(str1), len(str2), len(str3)
    print(length1, length2, length3 )
    # 构建一个三维数组
    c3Mat = []
    for ii in range(length1 +1):
        row = []
        for jj in range(length2+1):
            col = []
            for kk in range(length3+1):
                col.append(0)
            row.append(col)
        c3Mat.append(row)

    for i in range(1,length1):
        for j in range(1,length2):
            for k in range(1,length3):
                if str1[i] == str2[j] and str2[j] == str3[k]:
                    c3Mat[i + 1][j + 1][k + 1] = c3Mat[i][j][k] +1
                elif str1[i] == str2[j] and str1[i] != str3[k]:
                    c3Mat[i + 1][j + 1][k + 1] = max1(c3Mat[i+1][j+1][k], c3Mat[i][j][k+1])
                elif str1[i] == str3[k] and str1[i] != str2[j]:
                    c3Mat[i + 1][j + 1][k + 1] = max1(c3Mat[i+1][j][k+1], c3Mat[i][j+1][k])
                elif str2[j] == str3[k] and str1[i] != str2[j]:
                    c3Mat[i + 1][j + 1][k + 1] = max1(c3Mat[i][j+1][k+1], c3Mat[i+1][j][k])
                else:
                    c3Mat[i + 1][j + 1][k + 1] = max2(c3Mat[i][j+1][k+1],c3Mat[i+1][j][k+1],c3Mat[i+1][j+1][k],c3Mat[i][j][k+1],c3Mat[i][j+1][k],c3Mat[i+1][j][k])

    length = c3Mat[length1][length2][length3]
    return length

if __name__ == '__main__':
    aString = 'ABCBDAB'
    bString = 'BDCABA'
    cString = 'FEBCBA'
    length = GetMLCSLength(aString, bString,cString)
    print("最长公共子序列的长度为：",length)
