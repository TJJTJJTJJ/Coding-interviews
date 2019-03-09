# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        result1 = [root.val]
        result2 = [root]
        self.PrintLeftRight(result1, result2)
        return result1
        
    def PrintLeftRight(self, result1, result2):
        if len(result2) == 0:
            return None
        if result2[0].left!=None:
            result1.append(result2[0].left.val)
            result2.append(result2[0].left)
        if result2[0].right!=None:
            result1.append(result2[0].right.val)
            result2.append(result2[0].right)
        result2.pop(0)
        self.PrintLeftRight(result1, result2)