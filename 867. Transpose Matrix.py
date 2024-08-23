class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])

        transposed_matrix = []
        for _ in range(n):
            transposed_matrix.append([0] * m)
        
        for i in range(m):
            for j in range(n):
                transposed_matrix[j][i] = matrix[i][j]
        
        return transposed_matrix

       
