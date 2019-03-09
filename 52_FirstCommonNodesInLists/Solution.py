# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1==None or pHead2==None:
            return None
        # calculate the counts
        len1 = 0
        pNode1 = pHead1
        while pNode1!=None:
            len1+=1
            pNode1 = pNode1.next
        pNode1 = pHead1
        len2 = 0
        pNode2 = pHead2
        while pNode2!=None:
            len2+=1
            pNode2 = pNode2.next
        pNode2 = pHead2
        # calculate the diff
        if len1>len2:
            lendiff = len1-len2
            while lendiff:
                pNode1 = pNode1.next
                lendiff-=1
        else:
            lendiff = len2-len1
            while lendiff:
                pNode2 = pNode2.next
                lendiff-=1
        while pNode1!=None and pNode2!=None and pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1


# Solution2
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1==None or pHead2 == None:
            return None
        stack1 = []
        pNode1 = pHead1
        while pNode1:
            stack1.append(pNode1)
            pNode1 = pNode1.next
        
        stack2 = []
        pNode2 = pHead2
        while pNode2:
            stack2.append(pNode2)
            pNode2 = pNode2.next
        res = None
        while len(stack1) and len(stack2):
            if stack1[-1]==stack2.pop():
                res = stack1.pop()
                
        return res