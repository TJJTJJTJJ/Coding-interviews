# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        if pHead.next == None:
            return None
        
        num = self.Numbers(pHead)
        if num==0:
            return None
        p1 = pHead
        p2 = pHead
        for i in range(num):
            p2=p2.next
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p1
        
    
    def Numbers(self, pHead):
        p1 = pHead
        p2 = pHead.next
        while p1!=p2 and p2.next!=None and p2!=None:
            p1 = p1.next
            p2 = p2.next.next
          #  if p1 == p2:
         #       break
        if p1!=p2:
            return 0
        num = 1
        p2 = p2.next
        while p1!=p2:
            p2 = p2.next
            num += 1
        return num