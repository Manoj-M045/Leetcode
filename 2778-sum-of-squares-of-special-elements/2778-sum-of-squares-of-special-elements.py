class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        length=len(nums)
        for i in range(len(nums)):
            if(length%(i+1)==0):
                s=s+nums[i]**2
        return s

        