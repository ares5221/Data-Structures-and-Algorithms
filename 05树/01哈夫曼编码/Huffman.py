#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
设计算法，给一个字符串进行二进制编码，使得编码后字符串的长度最短。
ord（）函数就是用来返回单个字符的ascii值（0-255）或者unicode数值（）
chr（）函数是输入一个整数【0，255】返回其对应的ascii符号
"""
def CalFrequency(src, pWeight):
    if len(src) == 0:
        return
    for i in range(len(src)):
        if ord(src[i]) is not None:
            pWeight[ord(src[i])] += 1
    # print('origin pWeight', pWeight)

def GetCharFreqs(pWeight,chars_frequs):
    for j in range(len(pWeight)):
        if pWeight[j] != 0:
            # print('字符：', chr(j), '--ASCII：', j, '--频数', pWeight[j])
            chars_frequs.append(tuple((chr(j), pWeight[j])))
    print('字符出现频数：', chars_frequs)
    return chars_frequs

#Tree-Node Type
class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
    def isLeft(self):
        return self.father.left == self

#create nodes创建叶子节点
def CreateNodes(freqs):
    return [Node(freq) for freq in freqs]

#create Huffman-Tree创建Huffman树
def CreateHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

#Huffman编码
def HuffmanCoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

if __name__ == '__main__':
    MAX_SIZE = 256
    src = 'When u r old and grey and full of sleep,' \
          'And nodding by the fire, take down this book,' \
          'And slowly read, and dream of the soft look' \
          'Your eyes had once, and of their shadows deep;' \
          'How many loved ur moments of glad grace,' \
          'And loved ur beauty with love false or true,' \
          'But one man loved the pilgrim soul in u,' \
          'And loved the sorrows of ur changing face;' \
          'And bending down beside the glowing bars,' \
          'Murmur, a little sadly, how Love fled' \
          'And paced upon upon the mountains overhead' \
          'And hid his face amid a crowd of stars.'
    pWeight = [0] * MAX_SIZE # 声明权重数组
    CalFrequency(src, pWeight) # 计算每个字符出现次数
    chars_frequs = []
    chars_frequs = GetCharFreqs(pWeight,chars_frequs) # 计算出现字符频数
    nodes = CreateNodes([item[1] for item in chars_frequs])
    root = CreateHuffmanTree(nodes)
    codes = HuffmanCoding(nodes, root)
    for item in zip(chars_frequs, codes):
        print('Character:%s freq:%-2d   encoding: %s' % (item[0][0], item[0][1], item[1]))