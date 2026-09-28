class Solution:
    def sortColors(self, nums: List[int]) -> None:
        s=0
        m=0
        e=len(nums)-1
        while(m<=e):
            if(nums[m]==2):
                nums[m],nums[e]=nums[e],nums[m]
                e-=1
            elif(nums[m]==1):
                m+=1
            else:
                nums[s],nums[m]=nums[m],nums[s]
                s+=1
                m+=1
        return nums  