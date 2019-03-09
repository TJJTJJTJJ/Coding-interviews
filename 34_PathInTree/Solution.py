# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None or root.val > expectNumber:
            return False
        result1 = []
        result2 = []
        self.FindPath2(root, expectNumber, result1, result2)
        result = sorted(result1, key=lambda x:len(x), reverse=True)
        return result
        
    def FindPath2(self, root, expectNumber, result1, result2):
        if root == None or root.val > expectNumber:
            return None
        result2.append(root.val)
        if root.left == None and root.right == None and root.val == expectNumber:
            result1.append(result2)
        self.FindPath2(root.left, expectNumber-root.val, result1, result2[:])
        self.FindPath2(root.right, expectNumber-root.val, result1, result2[:])


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root==None or root.val > expectNumber:
            return []
        if root.val==expectNumber and root.left==None and root.right==None:
            return [[root.val]]
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        resultleft = []
        if len(left)!=0:
            resultleft = [ [root.val]+lef for lef in left]
        resultright = []
        if len(right)!=0:
            resultright = [[root.val]+rig for rig in right]
        result = resultleft+resultright
        result = sorted(result, key=lambda x:len(x), reverse=True)
        return result