class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=0
        w=0
        while(w<len(nums) and r<len(nums)):
            if(nums[r]!=val):
                nums[w]=nums[r]
                w+=1
                r+=1
            else:
                r+=1
        return w
        
        