class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=max(nums)
        p=[]
        for i in range(n+1):
            p.append(i)
        if(len(p)==len(nums)):
            s=max(p)+1
            return s
        for i in p:
            if(i not in nums):
                return i
        
        