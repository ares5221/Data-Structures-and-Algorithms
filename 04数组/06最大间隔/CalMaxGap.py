#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 定义桶
class tagSBucket:
    bValid = False
    nMin = nMax = 0
    def Add(self, n):
        if not self.bValid:
            self.nMin = self.nMax = n
            self.bValid = True
        else:
            if self.nMax < n:
                self.nMax = n
            elif self.nMin > n:
                self.nMin = n

# 计算数组中整数间存在的最大间隔
def CalcMaxGap(src):
    if src is None:
        return None
    slen = len(src)
    if slen <= 0:
        return 0
    pBucket = [tagSBucket() for i in src]

    # 求最值
    nMax, nMin = src[0], src[0]
    indexList = list(range(slen))
    for i in indexList:
        if nMax < src[i]:
            nMax = src[i]
        if nMin > src[i]:
            nMin = src[i]
    # print('src Max:',nMax, 'src Min:',nMin)

    # 依次将数据放入桶中
    delta = nMax - nMin
    for i in indexList:
        nBucket = int( ( (src[i] - nMin) / delta) * slen )
        if nBucket >= slen:
            nBucket = slen - 1
        pBucket[nBucket].Add(src[i])
    # for ppp in pBucket:
        # print( ppp.nMin, ppp.nMax)

    # 计算有效桶的间隔
    nGap = delta / slen  # 最小间隔结果
    i = 0  # 首个桶一定是有效的
    p = pBucket[0].nMax  # 记录最小间隔的两个值
    q = pBucket[0].nMin
    for j in indexList:
        if pBucket[j].bValid:
            gap = pBucket[j].nMin - pBucket[i].nMax
            if nGap < gap:
                nGap = gap
                p = pBucket[i].nMax
                q = pBucket[j].nMin
            i = j
    print('最大间隔的两个数为：%d 和 %d , 间隔为：%d' % (p, q, q - p))
    return nGap

if __name__ == '__main__':
    src = [1, 7, 14, 9, 4, 13]
    CalcMaxGap(src)