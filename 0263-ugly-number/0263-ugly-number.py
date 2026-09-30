class Solution:
    def isUgly(self, n: int) -> bool:
        if(n<=0):
            return False
        copy=n
        while(copy>1):
            if(copy%2==0):
                copy=copy//2
            elif(copy%3==0):
                copy=copy//3
            elif(copy%5==0):
                copy=copy//5
            else:
                return False
        
        return True
        
        