# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers==None or len(numbers)<5:
            return False
        transdict = {'A':1, 'J':11, 'Q':12, 'K':13}
        for i, val in enumerate(numbers):
            if val in transdict.keys():
                numbers[i] = transdict[val]
        numbers = sorted(numbers)
        for numbers_0, val in enumerate(numbers):
            if val != 0:
                break
        if numbers[-1]-numbers[numbers_0]>4:
            return False
        for j in range(numbers_0, len(numbers)):
            if numbers[j]==numbers[j-1]:
                return False
        return True