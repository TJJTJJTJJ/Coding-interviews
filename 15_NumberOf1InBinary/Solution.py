# v-3.0
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        INT_BITS = 32
        MAX_INT = (1<<(INT_BITS))-1
        count, i = 0, 1
        while i <= MAX_INT :
            if (i & n) != 0:
                count+=1
            i <<= 1
        return count

class Solution:
    def NumberOf1(self, n):
        # write code here
        INT_BITS = 32
        MAX_INT = (1<<(INT_BITS-1))-1
        count, i = 0, 1
        while i <= MAX_INT+1 :
            if (i & n) != 0:
                count+=1
            i <<= 1
        return count

# v-4.0
class Solution:
    def NumberOf1(self, n):
        # write code here
        INT_BITS = 32
        MAX_INT = (1<<INT_BITS)-1
        count = 0
        while n >= -MAX_INT and n != 0:
            n = (n-1)&n
            count += 1
        return count
# 正数一定会成为0，负数会一直变小到最小值
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff # 这个是直接把int变成float型， -10变成4294967286，变换前后1的个数不发生变换
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count
