#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
八皇后手动维护堆栈解法
"""
import queue
def EightQueen(board):
    blen = len(board)
    stack = queue.LifoQueue()  # 用后进先出队列来模拟一个栈
    stack.put((0,0))    # 为了自洽的初始化
    while not stack.empty():
        i,j = stack.get()
        if check(board,i,j):    # 当检查通过
            board[i] = j    # 别忘了放Queen
            if i >= blen - 1:
                print(board)   # i到达最后一行表明已经有了结果
                printBoard(board)
                # break
            else:
                if j < blen - 1:    # 虽然说要把本位置右边一格入栈，但是如果本位置已经是行末尾，那就没必要了
                    stack.put((i,j+1))
                stack.put((i+1,0))    # 下一行第一个位置入栈，准备开始下一行的扫描
        elif j < blen - 1:
            stack.put((i,j+1))    # 对于未通过检验的情况，自然右移一格即可

def check(board,row,col):
    i = 0
    while i < row:
        if abs(col-board[i]) in (0,abs(row-i)):
            return False
        i += 1
    return True

def printBoard(board):
    '''为了更友好地展示结果 方便观察'''
    import sys
    for i,col in enumerate(board):
        sys.stdout.write('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
        print(' ')

if __name__ == '__main__':
    queenNum = 8
    board = [0 for i in range(queenNum)]
    EightQueen(board)