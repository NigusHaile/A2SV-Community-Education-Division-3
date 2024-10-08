class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        count = 0
        for col in range(num_cols):
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        
        return count
