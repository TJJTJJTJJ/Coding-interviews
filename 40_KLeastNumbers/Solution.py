# -*- coding:utf-8 -*-
import heapq

class MyHeap(object):
    def __init__(self, input):
        self.data = [ -val for val in input]
        heapq.heapify(self.data)
    def pushpop(self, item):
        heapq.heappushpop(self.data, -item)
        

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput)<k:
            return []
        if len(tinput)==k:
            tinput.sort()
            return tinput
        
        stack = MyHeap(tinput[:k])
        for val in tinput[k:]:
            stack.pushpop(val)
            print(stack.data)
        res = [-val for val in stack.data]
        res.sort()
        return res


