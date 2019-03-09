
# v-0.02
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not isinstance(s, str) or len(s)<=0 or s is None :
            return ''
        
        spaceNum = 0
        
        for i in s:
            if i == " ":
                spaceNum += 1
        newStrLen = len(s) + 2*spaceNum
        newStrList = newStrLen * [None]
        
        indexOfNew, indexOfOriginal = newStrLen -1 , len(s)-1
        
        while indexOfNew>=0 :
            if s[indexOfOriginal] == ' ':
                newStrList[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStrList[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        newStr = ''.join(newStrList)
        return newStr