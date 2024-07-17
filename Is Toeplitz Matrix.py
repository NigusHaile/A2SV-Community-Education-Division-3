class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][column] != matrix[row-1][column-1]:
                    return False
        return True
        