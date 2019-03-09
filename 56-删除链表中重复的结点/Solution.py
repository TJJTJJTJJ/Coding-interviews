# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pH = ListNode(pHead.val-1)
        pH.next = pHead
        pre = pH
        first = pH.next
        last = first
        
        while last:
            if last.next and last.next.val == first.val:
                last = last.next
            else:
                if first==last:
                # 无重复
                    pre.next=last
                    pre = pre.next
                    first = pre.next
                    last = first
                else:
                # 有重复
                    first = last.next
                    last = first
        pre.next = last            
        return pH.next
