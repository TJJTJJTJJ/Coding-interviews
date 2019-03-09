# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss)==1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        charList2 = self.PermutationList(charList)
        charList3 = [ ''.join(val) for val in charList2]
        return charList3
        
    def PermutationList(self, charList):
        if len(charList)==1:
            return [charList]
        charListtmp3 = []
        for i in range(len(charList)):
            if i>0 and charList[i]==charList[i-1]:
                continue
            charListtmp = self.PermutationList(charList[0:i]+charList[i+1:])
            charListtmp2 = [charList[i:i+1]+val for val in charListtmp]
            charListtmp3 = charListtmp3 + charListtmp2
        return charListtmp3