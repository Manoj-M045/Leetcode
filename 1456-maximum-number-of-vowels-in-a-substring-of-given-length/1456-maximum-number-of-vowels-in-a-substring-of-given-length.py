class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ss=s[0:k]
        c=0
        for i in ss:
            if(i in "aeiou"):
                c+=1
        count=c
        for i in range(k,len(s)):
            if(s[i] in "aeiou"):
                count+=1
            if(s[i-k] in "aeiou"):
                count-=1
            if(count>c):
                c=count
        return c

        