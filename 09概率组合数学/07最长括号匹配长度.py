#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
给定字符串，仅包含左括号‘(’和右括号‘)’，它可能不是括号匹配的，设计算法，找出最长匹配的括号子串。

只有在右括号和左括号发生匹配时，才有可能更新最终解。
计算s[0…i]中左括号数目与右括号数目的差x，若x为0时，考察最终解是否可以更新，
这个差x是入栈的数目，代码中用“深度”deep表达。
由于可能出现左右括号不相等——尤其是左括号数目大于右括号数目，所以，再从右向左扫描一次。
用deep值替换stack栈，空间复杂度由O(N)降到O(1)。

'''
def match_longest_parentheses(s):
    size = len(s)
    li = []  # 记录最长结果的字符串索引，例如：对于"()(()"则返回[[0, 1], [3, 4]]
    deep = 0  # 遇到多少左括号
    start = 0  # 最深的(deep=0 时)左括号的位置
    for i in range(size):
        if s[i] == '(':
            deep += 1
        else:  # s[i] == ')'
            deep -= 1
            if deep == 0:
                if len(li) == 0 or li[0][1] - li[0][0] < i - start:
                    li = [[start, i]]
                elif li[0][1] - li[0][0] == i - start:
                    li.append([start, i])
            elif deep < 0:  # 说明右括号数目大于左括号数目
                deep = 0
                start = i + 1

    deep = 0  # 遇到多少右括号
    start = size - 1  # 最深的(deep=0 时)右括号的位置
    for i in range(size - 1, -1, -1):
        if s[i] == ')':
            deep += 1
        else:  # s[i] == '('
            deep -= 1
            if deep == 0:
                if len(li) == 0 or li[0][1] - li[0][0] < start - i:
                    li = [[i, start]]
                elif li[0][1] - li[0][0] == start - i and not li.__contains__([i, start]):
                    li.append([i, start])
            elif deep < 0:  # 说明左括号数目大于右括号数目
                deep = 0
                start = i - 1
    return li


if __name__ == '__main__':
    s = '()(()))(((((()))'
    print('字符串：%s' % s)
    li = match_longest_parentheses(s)
    print('最长括号索引：%s' % li)
    ss = [s[i[0]:i[1] + 1] for i in li]
    print('最长括号:%s' % ','.join(ss))
