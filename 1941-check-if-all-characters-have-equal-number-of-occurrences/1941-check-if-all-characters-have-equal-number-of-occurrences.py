class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        x=s.count(s[0])
        for i in range(1,len(s)):
            if(s.count(s[i])==x):
                continue
            else:
                return False
        return True
        