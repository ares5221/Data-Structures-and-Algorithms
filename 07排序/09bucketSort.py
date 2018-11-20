#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class node:
    def __init__(self, k):
        self.key = k
        self.next = None

def bucketsort(lista):
    h = []
    for i in range(0, 10):
        h.append(node(0))
    for i in range(0, len(lista)):
        tmp = node(lista[i])
        map = lista[i] // 10
        p = h[map]
        if p.key is 0:
            h[map].next = tmp
            h[map].key = h[map].key + 1
        else:
            while (p.next != None and p.next.key <= tmp.key):
                p = p.next
            tmp.next = p.next
            p.next = tmp
            h[map].key = h[map].key + 1
    k = 0
    for i in range(0, 10):
        q = h[i].next
        while (q != None):
            lista[k] = q.key
            k = k + 1
            q = q.next
    return lista


lista = [1, 4, 23, 45, 97, 22, 10, 4]  # 桶排序测试代码
bucketsort(lista)
print('桶排序：',lista)

