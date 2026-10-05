class Solution:
    def numOfSubarrays(self, nums: list[int], k: int, threshold: int) -> int:
        n=[]
        x=nums[0:k]
        s=sum(x)
        ss=s//k
        c=0
        if(ss>=threshold):
            c+=1
        for i in range(k,len(nums)):
            s=s+nums[i]-nums[i-k]
            ss=s//k
            if(ss>=threshold):
                c+=1
        return c
        