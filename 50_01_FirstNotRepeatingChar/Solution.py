# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None:
            return -1
        if len(s) == 1:
            return 0
            
        hashmap = MyHash(52)
        for val in s:
            hashmap.add(val)
        data = hashmap.get()
        for i, val in enumerate(s):
            index = hashmap.getindex(val)
            if data[index] == 1:
                return i
        return -1
        
        
class MyHash:
    def __init__(self, n):
        self.data = [0 for i in range(n)]
        
    def add(self, char):
        self.data[self.getindex(char)]+=1
        
    def getindex(self, char):
        if char < 'a':
            return ord(char)-ord('A')+26
        else:
            return ord(char)-ord('a')
    
    def getchar(self, index):
        return chr(index)
    
    def get(self):
        return self.data 