class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=[]
        n=set(nums)
        for i in range(1,len(nums)+1):
            if(i not in n):
                k.append(i)
        return k
        
        
        