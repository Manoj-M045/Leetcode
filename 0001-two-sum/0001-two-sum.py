class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        for i in range(len(nums)):
            need=target-nums[i]
            if(need in maps):
                return [maps[need],i]
            else:
                maps[nums[i]]=i