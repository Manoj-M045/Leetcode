class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sw=nums[:k]
        s=sum(sw)
        a=s/k
        for i in range(k,len(nums)):
            s=(s+nums[i])-nums[i-k]
            avg=s/k
            if(avg>a):
                a=avg
        return a

        