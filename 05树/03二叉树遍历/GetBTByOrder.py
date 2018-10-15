#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
根据二叉树的前序 中序遍历 求其后序遍历
'''
class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

def get_pre_deep(post, mid, a):
    if len(post) == 0 or len(mid) == 0:
        return
    a = [post[-1],]
    root = post[-1]
    root_index = mid.index(root)
    # 遍历左子树
    root_left = get_pre_deep(post[0:root_index], mid[0:root_index], a)
    # 遍历右子树
    root_right = get_pre_deep(post[root_index:-1], mid[root_index+1:], a)
    # 把所得到的结点连接,把返回结果为空的情况剔除
    if root_left is not None and root_right is not None:
        # 注意这两个值的连接顺序(和已知前序和中序相反)
        a.extend(root_left)
        a.extend(root_right)
    elif root_left is not None:
        a.extend(root_left)
    elif root_right is not None:
        a.extend(root_right)
    # a.append(root)
    return a

if __name__ == '__main__':
    # 已知的树的前序与中序遍历
    # pre = [1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10]
    # mid = [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7]
    pre = ['G','D','A','F','E','M','H','Z']
    mid = ['A','D','E','F','G','H','M','Z']
    # 方法一：通过前序中序而画出树，然后后序遍历该树
    head = get_tree(pre, mid)
    print ("方法一：通过前序中序而画出树，然后后序遍历该树：")
    after_deep_func2(head)

    # 方法二：通过前序中序直接递归得到其后序遍历
    print("方法二：通过前序中序直接递归得到其后序遍历为：")
    res = get_after_deep(pre, mid, [])
    print(res)#res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]

    #通过中序后序求前序遍历
    print("问题二：通过后序中序直接递归得到其前序遍历为：")
    post = ['A', 'E', 'F', 'D', 'H', 'Z', 'M', 'G']
    mid = ['A', 'D', 'E', 'F', 'G', 'H', 'M', 'Z']
    pre = get_pre_deep(post, mid, [])
    print(pre)


