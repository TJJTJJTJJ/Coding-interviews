# 第一种解法：同时删除两个不一样的数字
# 这种解法可以推广到数组中出现出现次数超过1/4的数字，需要三个辅助栈
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers==None:
            return 0
        if len(numbers)==1:
            return numbers[0]
        if len(numbers)&1==1:
            numbers.extend(numbers)
        stack = []
        for val in numbers:
            if len(stack)!=0 and val!=stack[-1]:
                stack.pop()
            else:
                stack.append(val)
        if len(stack)!=0:
            return stack[0]
        else:
            return 0


# 书上给出的解法无法证明其有效性和正确性，所以无法推广，有待进一步的证明。