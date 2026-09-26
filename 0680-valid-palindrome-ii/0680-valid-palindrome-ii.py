class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(x,y,s):
            while(x<y):
                if(s[x]!=s[y]):
                    return False
                x+=1
                y-=1
            return True
        if(s==s[::-1]):
            return True
        else:
            l=0
            r=len(s)-1
            while(l<r):
                if(s[l]!=s[r]):
                    return check(l+1,r,s) or check(l,r-1,s)
                l+=1
                r-=1
        return False
                    
        

        