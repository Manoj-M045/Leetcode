class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        copy=n
        while(copy>1):
            if(copy%3==0):
                copy=copy//3
            else:
                return False
        return True
        