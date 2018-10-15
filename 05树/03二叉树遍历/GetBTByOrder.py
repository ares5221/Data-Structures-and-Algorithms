#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# if __name__ == "__main__":
#     tree = Node(1, Node(2, Node(4), Node(5, Node(8), Node(9, left=Node(11)))), Node(3, Node(6), Node(7, left=Node(10))))

def get_tree(pre, mid):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return Node(pre[0])
    root = Node(pre[0])
    root_index = mid.index(pre[0])
    root.left = get_tree(pre[1:root_index + 1], mid[:root_index])
    root.right = get_tree(pre[root_index + 1:], mid[root_index + 1:])
    return root

def get_after_deep(pre, mid, a):
    if len(pre) == 1:
        a.append(pre[0])
        return
    if len(pre) == 0:
        return
    root = pre[0]
    root_index = mid.index(root)
    get_after_deep(pre[1:root_index+1], mid[:root_index], a)
    get_after_deep(pre[root_index+1:], mid[root_index+1:], a)
    a.append(root)
    return a

# 前序遍历（递归）
def pre_deep_func(root):
    if root is None:
        return
    print(root.value,end =' ')  # print 放到下一行 就是中序遍历，放到最后 就是后序遍历
    pre_deep_func(root.left)
    pre_deep_func(root.right)

def after_deep_func2(root):
    a = []
    b = []
    while a or root:
        while root:
            b.append(root.value)
            a.append(root)
            root = root.right
        h = a.pop()
        root = h.left
    print(b[::-1])

if __name__ == '__main__':
    # 已知的树的前序与中序遍历
    pre = [1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10]
    mid = [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7]
    # 通过前序中序得到的树
    head = get_tree(pre, mid)
    print ("通过前序中序得到的树后序遍历为：")
    after_deep_func2(head)

    # 通过前序中序得到的后序遍历
    res = get_after_deep(pre, mid, [])
    print ("\n",res)  #res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]
