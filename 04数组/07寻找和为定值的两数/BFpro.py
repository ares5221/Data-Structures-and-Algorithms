#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/9/10'
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
暴力求解
"""
def TwoNumSumPro(src, Sum):
    if src is None or len(src) == 1:
        return None
    res = []
    src.sort()
    start, end = 0, len(src) -1
    while start < end:
        if src[start] + src[end] == Sum:
            res.append((src[start], src[end]))
            start +=1
            end -=1
        else:
            if src[start] + src[end] < Sum:
                start +=1
            else:
                end -=1
    return res

if __name__ == '__main__':
    src = [1,3,4,6,9,2,5]
    Sum = 8
    res = TwoNumSumPro(src, Sum)
    print('和为：',Sum,'的两数为：',res)