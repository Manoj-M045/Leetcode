class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k=nums[:n]
        kk=nums[n:]
        i=0
        s=[]
        while(i<n):
            s.append(k[i])
            s.append(kk[i])
            i=i+1
        return s

        