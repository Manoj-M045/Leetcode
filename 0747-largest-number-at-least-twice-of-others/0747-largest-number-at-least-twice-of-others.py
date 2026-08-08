class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        copy=nums.copy()
        copy.sort()
        n=copy[-1]
        m=copy[-2]
        if(n>=(2*m)):
            for i in range(len(nums)):
                if(nums[i]==n):
                    return i
        return -1
        