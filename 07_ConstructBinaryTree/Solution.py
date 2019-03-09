# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 特殊边界
        if(pre is None or tin is None or len(pre)!=len(tin) or len(pre)==0):
            return None
        # 正常终止
        root = TreeNode(pre[0])
        if len(pre)==1 :
            return root
        # 不匹配的情况
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:(i+1)], tin[:i])
        root.right = self.reConstructBinaryTree(pre[(i+1):], tin[(i+1):])
        return root
