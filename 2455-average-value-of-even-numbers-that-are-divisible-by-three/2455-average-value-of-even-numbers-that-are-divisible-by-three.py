class Solution:
    def averageValue(self, nums: list[int]) -> int:
        c=0
        s=0
        for i in nums:
            if(i%2==0 and i%3==0):
                c+=1
                s=s+i
        if(c==0):
            return 0
        else:
            return s//c
        