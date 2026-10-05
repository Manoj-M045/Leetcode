class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        c=0
        n=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if(nums[i]!=nums[j] and nums[j]<nums[i]):
                    c+=1
            n.append(c)
        return n
            
        