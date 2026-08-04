class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=[]
        p=[]
        for i in range(min(nums),max(nums)+1):
            n.append(i)
        for i in n:
            if(i not in nums):
                p.append(i)
        return p
        