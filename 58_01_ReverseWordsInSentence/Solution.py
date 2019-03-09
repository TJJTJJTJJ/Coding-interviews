# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s or len(s)==0:
            return ''
        if len(s)==1:
            return s
        
        lis = list(s)
        lis = self.Reverse(lis)
        start=0
        end=0
        lis2 = []
        while end <= len(s)-1:
            if lis[end] == ' ':
                lis2.extend(self.Reverse(lis[start:end]))
                lis2.append(' ')
                end+=1
                start=end
            end+=1
        
        lis2.extend(self.Reverse(lis[start:end+1]))
        res = ''.join(lis2)
        return res
        
        
    def Reverse(self, lis):
        start = 0
        end = len(lis)-1
        while start<end:
            lis[start], lis[end] = lis[end], lis[start]
            start+=1
            end-=1
        return lis




# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s or len(s)<=0:
            return ''
        if len(s)==1:
            return s
        list1 = list(s)
        list2 = [' ' for i in range(len(s))]
        stack = []
        j = len(s)-1
        for i in range(len(s)+1):
            if i == len(s) or list1[i] == ' ':
                print(stack)
                print(list2)
                while len(stack):
                    list2[j] = stack.pop()
                    j-=1
                j-=1
            else:
                stack.append(list1[i])
        res = ''.join(list2)
        return res