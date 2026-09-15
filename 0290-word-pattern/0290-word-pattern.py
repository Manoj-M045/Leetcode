class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n={}
        words=s.split()
        if(len(pattern)!=len(words)):
            return False
        if(len(set(pattern))!=len(set(words))):
            return False
        for i in range(len(pattern)):
            if(pattern[i] in n):
                if(n[pattern[i]]!=words[i]):
                    return False
            else:
                n[pattern[i]]=words[i]
        return True

        
        