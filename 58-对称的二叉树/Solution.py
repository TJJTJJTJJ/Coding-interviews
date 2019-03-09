# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        flag = self.isLeftRight(pRoot.left, pRoot.right)
        return flag
        
    def isLeftRight(self, pLeft, pRight):
        
        if pLeft==None and pRight==None:
            return True
        if not (pLeft and pRight):
            return False
        if pLeft.val == pRight.val and self.isLeftRight(pLeft.left,pRight.right) and self.isLeftRight(pLeft.right, pRight.left):
            return True
        return False
            