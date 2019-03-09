# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV==None or popV==None:
            return False
        stack = []
        j=0
        for val in pushV:
            stack.append(val)
            while len(stack)>0 and stack[-1] == popV[j]:
                stack.pop()
                j+=1
        if len(stack)==0:
            return True
        else:
            return False
                
        