class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        ps=0
        maps={0:1}
        for i in range(len(nums)):
            ps=ps+nums[i]
            if(ps-k in maps):
                c=c+maps[ps-k]
            if(ps in maps):
                maps[ps]=maps[ps]+1
            else:
                maps[ps]=1
        return c
        
        