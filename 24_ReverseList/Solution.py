# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 特殊情况，空，一个结点
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        
        pNode = pHead
        pNext = pNode.next
        pPrev = None
        while pNext != None:
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
            pNext = pNode.next
        pNode.next = pPrev
        return pNode

# 这个时候的代码很冗长，根据github进行优化
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pNode = pHead
        pPrev = None
        while pNode != None:
            pNext = pNode.next
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pPrev

# 一般情况下，我还是会写出第一种代码，因为第一种代码方便，明了，第二种代码的可读性差一点