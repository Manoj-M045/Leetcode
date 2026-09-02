class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[]
        for i in nums:
            if(i%2==0):
                k.append(i)
        for i in k:
            nums.remove(i)
        j=0
        while(j<len(nums)):
            k.append(nums[j])
            j=j+1
        return k
        