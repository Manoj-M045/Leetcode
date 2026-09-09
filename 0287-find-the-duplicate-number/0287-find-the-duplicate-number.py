class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr=[0]*len(nums)
        for i in nums:
            if(arr[i]==0):
                arr[i]+=1
            else:
                arr[i]=arr[i]+1
        for i in range(len(arr)):
            if(arr[i]>1):
                return i
        