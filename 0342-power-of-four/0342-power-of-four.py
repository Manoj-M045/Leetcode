class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        copy=n
        while(copy>1):
            if(copy%4==0):
                copy=copy//4
            else:
                return False
        return True