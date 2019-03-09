# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence)==0:
            return False
        min = None
        max = None
        return self.VerifySquence(sequence, min, max)
    
    def VerifySquence(self, sequence, min, max):
        if min != None and min>sequence[-1]:
            return False
        if max != None and sequence[-1]>max:
            return False
        if len(sequence)==1:
            return True
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                break
        if i == 0:
            return self.VerifySquence(sequence[0:-1], sequence[-1], max)
        elif i == len(sequence)-1:
            return self.VerifySquence(sequence[0:-1], min, sequence[-1])
        else:
            return self.VerifySquence(sequence[0:i], min, sequence[-1]) and self.VerifySquence(sequence[i:-1], sequence[-1], max)