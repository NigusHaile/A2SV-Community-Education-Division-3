class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        index=0
        for j in range(n):
            if nums[j]!=0:
                nums[index], nums[j]=nums[j], nums[index]
                index+=1
        return nums
