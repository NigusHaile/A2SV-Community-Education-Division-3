class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maximum_right = -1 

        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = maximum_right
            maximum_right = max(maximum_right, current)
        
        return arr
