class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[0]*len(nums)
        pos=len(nums)-1
        l=0
        r=len(nums)-1
        while(l<=r):
            if(abs(nums[l])>=abs(nums[r])):
                n[pos]=nums[l]*nums[l]
                l=l+1
            else:
                n[pos]=nums[r]*nums[r]
                r=r-1
            pos-=1
        return n
        