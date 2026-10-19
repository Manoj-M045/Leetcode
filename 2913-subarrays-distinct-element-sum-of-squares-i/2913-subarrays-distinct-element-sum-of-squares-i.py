class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                x=nums[i:j]
                s=s+(len(set(x))**2)
        return s
        
        