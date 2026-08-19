class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        p=1
        s=1
        for i in range(len(nums)):
            ans[i]=p
            p=p*nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*s
            s=s*nums[i]
        return ans
        
            

        