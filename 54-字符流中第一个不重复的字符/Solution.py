# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.lis = []
    def FirstAppearingOnce(self):
        while len(self.lis)>0 and self.dic[self.lis[0]]==2:
            self.lis.pop(0)
        if len(self.lis)==0:
            return '#'
        else:
            return self.lis[0]
        # write code here
    def Insert(self, char):
        # write code here
        if char not in self.dic.keys():
            self.dic[char]=1
            self.lis.append(char)
        else:
            self.dic[char]=2