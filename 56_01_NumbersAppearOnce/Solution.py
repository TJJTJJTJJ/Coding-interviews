# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == None:
            return []
        xor = 0
        for val in array:
            xor ^= val
        idxOf1 = self.getFirstIdx(xor)
        if idxOf1 == 32:
            return []
        num1, num2 = 0, 0
        
        for val in array:
            if self.IsBit(val, idxOf1):
                num1 ^= val
            else:
                num2 ^= val
        return [num1, num2]
        
    def getFirstIdx(self, num):
        idx = 0
        while num & 1==0 and idx <=32:
            idx+=1
            num = num >>1
        return idx
    
    def IsBit(self, num, idx):
        num = num>>idx
        return num&1