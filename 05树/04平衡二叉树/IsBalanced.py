#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断一个树是否平衡
todo
代码有问题，待解决
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced2(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return height(root) != -1

if __name__ == '__main__':
    ss = Solution()
    # tree = [3,9,20,None,None,15,7]
    tree = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = TreeNode(tree)
    isBalanced = ss.isBalanced2(root)
    print(tree, 'is ', isBalanced)
