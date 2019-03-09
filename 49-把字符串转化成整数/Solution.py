# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        flag = False
        if not s and len(s)<=0:
            return 0
        num = 0
        numdict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        num_pm = 0
        for i in s:
            if i in numdict.keys():
                num = num*10+numdict[i]
                num_pm = 3
            elif i == '+' or i == '-' and num_pm <2:
                num_pm=3
            else:
                return 0
        if num == 0:
            flag = True
        if s[0]=='-':
            num = 0-num
        return num