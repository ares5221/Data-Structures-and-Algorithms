#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
给定某正整数N，统计从1到N！的所有数字中，首位数字出现1的概率
及首位为2,3...9的概率
及第二位为1...9的概率
数字1...9出现的概率分别为0.301/0.176/0.125/0.097/0.079/0.067/0.058/0.051/0.046
结论：我们会发现数字1出现的概率占总数的三成，此为本福特定律，也就是
第一数字定律，在阶乘，素数数列，斐波那契数列首位及住宅地址号码
可用于经济数据反欺诈 选举投票反欺诈
'''
import matplotlib.pyplot as plt
def first_num(n):
    while n >= 10:
        n = n//10
    return n

def second_num(n):
    while n >= 100:
        n = n//10
    return n%10

if __name__ == '__main__':
    n = 1
    frequence = [0 for i in range(0,10,1)]
    frequence2 = [0 for i in range(0, 10, 1)]

    for i in range(1,1000):
        n = n*i
        m = first_num(n)
        frequence[m] = frequence[m] + 1
        m2 = second_num(n)
        frequence2[m2] = frequence2[m2] + 1
    print('首位数字出现的频次',frequence)
    print('次位数字出现的频次',frequence2)

    x=[0,1,2,3,4,5,6,7,8,9]
    # in 'bo-', b is blue, o is O marker, - is solid line and so on
    plt.plot(x,frequence, 'bo-',label='首位数字', markersize=8)
    #bo-  gv-  ys-  ch-  mD-
    plt.plot(x,frequence2, 'mD-',label='次位数字', markersize=8)
    plt.grid(True)

    # plt.legend(loc="lower right")  # set legend location
    # plt.ylabel('Percentage')  # set ystick label
    # plt.xlabel('Difference')  # set xstck label
    # axes.grid(True)  # add grid
    # plt.savefig('D:\\commonNeighbors_CDF_snapshots.eps', dpi=1000, bbox_inches='tight')
    plt.show()


