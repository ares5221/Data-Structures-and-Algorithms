#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Some basic testing for your code is provided below. DO NOT modify
# these tests. Your code MUST pass these tests. Note, however, that
# passing these tests does not guarantee that your algorithm is
# correct. You should carry out more testing!


def find_stable_matching(MP, WP):
    """ The input of this function is defined by two lists MP and WP
    Men and women are numbered 0 through n-1
    MP[i] encodes the ith man's preferences. It is simply a list
    containing the numbers 0, 1, ... , n-1 in some order
    WP[i] encodes the ith woman's preferences. It is simply a list
    containing the numbers 0, 1,... , n-1 in some order
    The output is defined by a list of pairs of the form (i,j)
    indicating that man i is married to woman j
    Your output should be the man-optimal stable matching found by the
    GS-algorithm. """

    n = len(MP)
    isManFree = [True] * n
    isWomanFree = [True] * n
    # isManProposed=[[False]*n]*n
    isManProposed = [[False for i in range(n)] for j in range(n)]
    match = [(-1, -1)] * n

    while (True in isManFree):
        indexM = isManFree.index(True)
        if (False in isManProposed[indexM]):
            indexW = -1
            for i in range(n):
                w = MP[indexM][i]
                if (not isManProposed[indexM][w]):
                    indexW = w
                    break
            isManProposed[indexM][indexW] = True
            if (isWomanFree[indexW]):
                # isManProposed[indexM][indexW]=True
                isWomanFree[indexW] = False
                isManFree[indexM] = False
                match[indexM] = (indexM, indexW)
            else:
                indexM1 = -1
                for j in range(n):
                    if (match[j][1] == indexW):
                        indexM1 = j
                        break
                if (WP[indexW].index(indexM) < WP[indexW].index(indexM1)):
                    isManFree[indexM1] = True
                    isManFree[indexM] = False
                    match[indexM] = (indexM, indexW)
    print(match)
    return match


def test1():
    """ basic test for your code """
    MP = [[0, 1], [1, 0]]
    WP = [[0, 1], [0, 1]]
    SM = find_stable_matching(MP, WP)
    assert ((0, 0) in SM and (1, 1) in SM)


def test2():
    """ basic test for your code """
    MP = [[0, 1], [0, 1]]
    WP = [[0, 1], [0, 1]]
    SM = find_stable_matching(MP, WP)
    assert ((0, 0) in SM and (1, 1) in SM)


def test3():
    """ basic test for your code """
    MP = [[0, 1], [0, 1]]
    WP = [[1, 0], [1, 0]]
    SM = find_stable_matching(MP, WP)
    assert ((0, 1) in SM and (1, 0) in SM)


if __name__ == "__main__":
    print("**********test1************")
    test1()
    print("**********test2************")
    test2()
    print("**********test3************")
    test3()
