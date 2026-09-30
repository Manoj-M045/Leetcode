class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        n=[]
        for i in nums:
            copy=i
            count=0
            while(copy>0):
                count+=1
                copy=copy//10
            if(count%2==0):
                n.append(i)
        return len(n)
        