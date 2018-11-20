#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 堆排序
# 构造堆
class Heap_array:
    def __init__(self, array, size):
        self.array = array
        self.size = size


# 2 调整大顶堆
def Max_Heapify(Heap, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left < Heap.size and Heap.array[largest] < Heap.array[left]:
        largest = left
    if right < Heap.size and Heap.array[largest] < Heap.array[right]:
        largest = right
    if largest != i:
        Heap.array[largest], Heap.array[i] = Heap.array[i], Heap.array[largest]
        Max_Heapify(Heap, largest)


def Build_max_Heap(Heap):
    for i in range((Heap.size // 2) - 1, -1, -1):
        Max_Heapify(Heap, i)


def Heap_sort(array):
    if not array:
        return None
    if len(array) == 1:
        return array
    Heap = Heap_array(array, len(array))
    # print(Heap.array)
    # 1 构造大顶堆
    Build_max_Heap(Heap)
    for i in range(len(array) - 1, 0, -1):
        Heap.array[0], Heap.array[i] = Heap.array[i], Heap.array[0]
        Heap.size -= 1
        Max_Heapify(Heap, 0)
    return Heap.array


if __name__ == '__main__':
    srcArr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    resArr = Heap_sort(srcArr)
    print('堆排序结果：', resArr)
