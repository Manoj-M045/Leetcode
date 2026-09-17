class Solution:
    def isSubsequence(self, s: str, t: str) -> bool :
        st=0
        sts=0
        c=0
        while(st<len(s) and sts<len(t)):
            if(s[st]==t[sts]):
               st=st+1
               sts=sts+1
               c=c+1
            else:
               sts=sts+1
        if(c==len(s)):
            return True
        else:
            return False
        