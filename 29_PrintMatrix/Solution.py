# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == None:
            return []
        rowEnd = len(matrix)-1
        colEnd = len(matrix[0])-1
        rowStart = 0
        colStart = 0
        direction = 0
        result = []
        self.printMatrixDirectoin(matrix, rowStart, rowEnd, colStart, colEnd, direction, result)
        return result
        
    def printMatrixDirectoin(self, matrix, rowStart, rowEnd, colStart, colEnd, direction, result):
        if rowStart>rowEnd or colStart>colEnd :
            return None
        # 左到右
        if direction == 0:
            for j in range(colStart, colEnd+1):
                result.append(matrix[rowStart][j])
            rowStart+=1
        # 上到下
        if direction == 1:
            for i in range(rowStart, rowEnd+1):
                result.append(matrix[i][colEnd])
            colEnd-=1
        # 右到左
        if direction == 2:
            for j in range(colEnd, colStart-1, -1):
                result.append(matrix[rowEnd][j])
            rowEnd-=1
        # 下到上
        if direction == 3:
            for i in range(rowEnd, rowStart-1, -1):
                result.append(matrix[i][colStart])
            colStart+=1
        direction = (direction+1)%4
        self.printMatrixDirectoin(matrix, rowStart, rowEnd, colStart, colEnd, direction, result)