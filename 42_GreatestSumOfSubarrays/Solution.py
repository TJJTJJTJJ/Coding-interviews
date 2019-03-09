# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == None or len(array)==0:
            return 0
        maxstart = -1
        maxend = -1
        maxsum = -1
        nowsum = 0
        nowstart = 0
        nowend = -1
        for i, val in enumerate(array):
            nowsum += val
            if nowsum <= 0:
                nowsum = 0
                nowstart = i+1
                nowend = i+1
                continue
            nowend = i
            if nowsum > maxsum:
                maxsum = nowsum
                maxstart = nowstart
                maxend = nowend
        return maxsum