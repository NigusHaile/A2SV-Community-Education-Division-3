class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        maxLocal = []
        for _ in range(n - 2):
            maxLocal.append([0] * (n - 2))  
        for i in range(n - 2):
            for j in range(n - 2):
                #maximum value is initialize to nagetive infinity
                max_value = float('-inf')  
                
                for x in range(3):
                    for y in range(3):
                        max_value = max(max_value, grid[i + x][j + y])
                
                maxLocal[i][j] = max_value
        
        return maxLocal
