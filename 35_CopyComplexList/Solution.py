# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead==None:
            return None
        pHead = self.CloneNodes(pHead)
        pHead = self.ConnectRandomNodes(pHead)
        pHead1, pHead2 = self.ReconnectNodes(pHead)
        return pHead2
        
    def CloneNodes(self, pHead):
        pH = pHead
        while pHead:
            pNewNode = RandomListNode(pHead.label)
            pNext = pHead.next
            pHead.next = pNewNode
            pNewNode.next = pNext
            pHead = pNext
        return pH
    
    def ConnectRandomNodes(self, pHead):
        pH = pHead
        while pHead:
            if pHead.random:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next
        return pH
    
    def ReconnectNodes(self, pHead):
        pHori = pHead
        pHnew = pHead.next
        pHead2 = pHead.next
        while pHead2.next:
            pHead.next = pHead.next.next
            pHead2.next = pHead2.next.next
            pHead = pHead.next
            pHead2 = pHead2.next
        pHead.next  = pHead.next.next
        return pHori, pHnew


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class RandomSbListNode(RandomList):
    def __init__(self, x):
        self.label = x.label
        self.next = x.next
        self.random = x.random
        self.sb = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pHeadsb = self.CloneNodes(pHead)
        pHeadClone = self.ReconnectNodes(pHeadsb)
    
        
    def CloneNodes(self, pHead):
        pNode = pHead
        pHeadsb = RandomSbListNode(pNode)
        pClonePre = RandomListNode(pNode.val)
        pNodesb = pHeadsb
        pNodesb.sb = pClone
        pNode = pNode.next
        while pNode:
            pNew = RandomSbListNode(pNode)
            pClone = RandomListNode(pNode.val)
            pNew.sb = pClone
            pClonePre.next = pClone
            pClonePre = pClone
            pNode = pNode.next
        return pHeadsb
    
    def ReconnectNodes(self, pHeadsb):
        pHeadClone = pHeadsb.sb
        pNodesb = pHeadsb
        while pNodesb:
            if pNodesb.random:
                pNodesb.sb.random = pNodesb.random.sb
        return pHeadClone