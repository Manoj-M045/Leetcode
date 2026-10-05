class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        x=arr[0:3]
        c=0
        for i in x:
            if(i%2!=0):
                c+=1
        if(c==3):
            return True
        for i in range(3,len(arr)):
            if(arr[i]%2!=0):
                c+=1
            if(arr[i-3]%2!=0):
                c-=1
            if(c==3):
                return True
        return False
        