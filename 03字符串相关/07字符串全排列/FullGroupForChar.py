#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
递归求字符串的全组合
'''
def FGroup(ss):
    if not len(ss):
        return None
    if len(ss) == 1:
        return list(ss)
    charList = list(ss)
    charList.sort()
    pStr = []
    for i in range(len(charList)):
        pStr.append(charList[i])
        if i > 0 and charList[i] == charList[i - 1]:
            continue
        temp = FGroup(''.join(charList[i + 1:]))
        for j in temp:
            pStr.append(charList[i] + j)
        pStr = list(set(pStr))
        pStr.sort()
    return pStr

if __name__ == '__main__':
    src = 'abc'
    res = FGroup(src)
    for i in res:
        print(i)