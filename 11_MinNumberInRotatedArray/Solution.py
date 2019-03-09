# -*- coding:utf-8 -*-
# v-2 二分法-递归
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 异常情况：数组为空或者为none
        if rotateArray is None or len(rotateArray)==0 :
            return 0
        # 特殊情况：数组没有旋转或者只有一个值
        p = 0
        q = len(rotateArray)-1
        if rotateArray[p] < rotateArray[q] or p==q:
            return rotateArray[p]
        # 正常情况
        return self.minNumberInRotate_equal(rotateArray[:])
        
    def minNumberInRotate(self, rotateArray):
        p = 0
        q = len(rotateArray)-1
        mid = (p+q)/2
        # 正常情况
        # 结束条件
        if q-p == 1:
            return rotateArray[q]
        if rotateArray[p] <= rotateArray[mid]:
            return self.minNumberInRotate(rotateArray[mid:(q+1)])
        else:
            return self.minNumberInRotate(rotateArray[p:(mid+1)])
    
    def minNumberInRotate_equal(self, rotateArray):
        p =0
        q = len(rotateArray)-1
        mid = (p+q)/2
        # 特殊情况：有相同的数字，无法判断mid属于哪里
        if rotateArray[p]==rotateArray[mid] and rotateArray[p]==rotateArray[q] :
            if rotateArray[p] < rotateArray[p+1] :
                return rotateArray[p]
            else:
                return self.minNumberInRotate_equal(rotateArray[1:])
        else:
            return self.minNumberInRotate(rotateArray[p:(q+1)])