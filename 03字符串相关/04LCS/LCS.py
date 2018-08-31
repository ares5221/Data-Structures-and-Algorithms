#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
最长公共子序列
"""
def GetLCSLength(aString, bString, aLength, bLength):

    cMat = [[0 for i in range(bLength+1)] for j in range(aLength+1)]
    fMat = [[0 for i in range(bLength+1)] for j in range(aLength+1)]
    for i in range(aLength):
        for j in range(bLength):
            if aString[i] == bString[j]:
                cMat[i + 1][j + 1] = cMat[i][j] +1
                fMat[i + 1][j + 1] = 'OK'
            elif cMat[i + 1][j] > cMat[i][j + 1]:
                cMat[i + 1][j + 1] = cMat[i + 1][j]
                fMat[i + 1][j + 1] = 'Left'
            else:
                cMat[i + 1][j + 1] = cMat[i][j + 1]
                fMat[i + 1][j + 1] = 'Up'
    for i in cMat:
        print(i)
    print('')
    for j in fMat:
        print(j)
    print('')
    return cMat, fMat

def GetLCSString(aString, fMat, i, j):
    if i == 0 or j == 0:
        return
    if fMat[i][j] == 'OK':
        GetLCSString(aString, fMat, i-1, j-1)
        print(aString[i-1],end='')
    elif fMat[i][j] == 'Left':
        GetLCSString(aString,fMat,i,j-1)
    else:
        GetLCSString(aString,fMat,i-1,j)

if __name__ == '__main__':
    # aString = 'ABCBDAB'
    # bString = 'BDCABA'
    aString = "a1b2c3"
    bString = "1a1wbz2c123a1b2c123";
    aLength = len(aString)
    bLength = len(bString)
    cMat,fMat = GetLCSLength(aString, bString,aLength,bLength)
    GetLCSString(aString, fMat, aLength, bLength)