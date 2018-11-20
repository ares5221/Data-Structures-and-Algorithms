#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
给定一个链表和一个值x，将链表划分成两部分，使得划分后小于x的结点在前，大于
等于x的结点在后。在这两部分中要保持原链表中的出现顺序。
如：给定链表1->4->3->2->5->2和x = 3，返回1->2->2->4->3->5。

分别申请两个指针p1和p2，小于x的添加到p1中，大于等于x的添加到p2中；
最后，将p2链接到p1的末端即可。
时间复杂度是O(N)，空间复杂度为O(1)；该问题其实说明：快速排序对于单链表存储结构仍然适用
'''

#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None or head.next is None:
            return head
        node = ListNode(-999999)
        node.next = head
        head = node

        follow = head
        pre = head
        # 找到第一个值大于x的节点
        while follow is not None and follow.val < x:
            pre = follow
            follow = follow.next
        # 所有节点都小于x，直接返回原head
        if follow is None: return head.next
        # 遍历链表,此时pre是follow的上一个节点
        while follow.next is not None:
            if follow.next.val < x:
                # 删除原节点
                other = follow.next
                follow.next = follow.next.next
                # 将其值插入到pre之后
                tmp = pre.next
                other.next = tmp
                pre.next = other
                pre = pre.next
                continue
            follow = follow.next
        return head.next

if __name__ == '__main__':
    s1 = Solution()
    src = [1,4,3,2,5,2]
    s2 = [0 for i in range(len(src))]
    s2[0]=ListNode(1,4)
    s2[1] = ListNode(4, 3)
    s2[2] = ListNode(3, 2)
    s2[3]=ListNode(2,5)
    s2[4] = ListNode(5, 2)
    s2[5] = ListNode(2)
    print(s2[0])
    res = s1.partition(s2,3)
    while res.next:
        print(res.val)