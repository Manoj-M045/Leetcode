class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        k=[]
        for i in range(n,101):
            copy=i
            p=1
            while(i>0):
                p=p*(i%10)
                i=i//10
            if(p%t==0):
                k.append(copy)
        return min(k)
        