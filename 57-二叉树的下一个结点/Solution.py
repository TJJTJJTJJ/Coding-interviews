# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        # right tree exists
        if pNode.right:
            return self.GetRight(pNode)
        # right tree doesn't exists
        if not pNode.right:
            return self.GetFather(pNode)
        
        
    def GetRight(self, pNode):
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    
    def GetFather(self, pNode):
        while pNode.next and pNode.next.left!=pNode:
            pNode = pNode.next
        return pNode.next
        
        
        