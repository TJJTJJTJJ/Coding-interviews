# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        Head, Tail = self.ConvertHeadTail(pRootOfTree)
        return Head
    
    
    def ConvertHeadTail(self, pRoot):
        if pRoot==None:
            return None, None
        if pRoot.left==None and pRoot.right==None:
            leftHead = pRoot
            rightTail = pRoot
            return leftHead, rightTail
        if pRoot.left:
            leftHead, leftTail = self.ConvertHeadTail(pRoot.left)
            leftTail.right = pRoot
            pRoot.left = leftTail
        else:
            leftHead, leftTail = pRoot, pRoot
        if pRoot.right:
            rightHead, rightTail = self.ConvertHeadTail(pRoot.right)
            rightHead.left = pRoot
            pRoot.right = rightHead
        else:
            rightHead, rightTail = pRoot, pRoot

        return leftHead, rightTail