# v-2.0
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        self.dic = {False:self.Sum0, True:self.SumN}
        return self.SumN(n)
        
    def Sum0(self, n):
        return 0
        
    def SumN(self, n):
        return self.dic[not not n](n-1)+n

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        self.dic = {False:self.Sum0, True:self.SumN}
        return self.SumN(n)
        
    def Sum0(self, n):
        return 0
        
    def SumN(self, n):
        return self.dic[not not (n-1)](n-1)+n

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and self.Sum_Solution(n-1)+n