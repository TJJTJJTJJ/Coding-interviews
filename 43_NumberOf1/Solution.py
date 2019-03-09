# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ones = 0
        m = 1
        while m<=n:
            i = n//m%10
            a = n//(m*10)*(m*10)
            b = n%m
            if i == 0:
                ones += a/10
            elif i == 1:
                ones += a/10+b+1
            else:
                ones += a/10+m
            m*=10
        return ones