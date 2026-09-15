class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1={}
        n2={}
        k=[]
        for i in nums1:
            if i in n1:
                n1[i]=n1[i]+1
            else:
                n1[i]=1
        for i in nums2:
            if i in n1:
                if(n1[i]>0):
                    k.append(i)
                    n1[i]=n1[i]-1
        return k
               
        