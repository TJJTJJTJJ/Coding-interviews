class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == [[]] or len(array[0]) < 0:
            return False
        
        row = len(array)
        col = len(array[0])
        
        i = row -1
        j = 0
        
        if array[0][0] > target and array[row-1][col-1] < target:
            return False
        
        while (i>=0 and j<col) :
            if array[i][j] == target :
                return True
            if array[i][j] < target :
                j=j+1
            else:
                i=i-1
        return False