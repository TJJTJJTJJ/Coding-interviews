# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2==None:
            return False
        if pRoot1==None:
            return False
        result = False
        if pRoot1.val==pRoot2.val:
            result = self.HasSubtree2(pRoot1, pRoot2)
        if not result:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return result
    def HasSubtree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.HasSubtree2(pRoot1.left, pRoot2.left) and self.HasSubtree2(pRoot1.right, pRoot2.right)
        return False