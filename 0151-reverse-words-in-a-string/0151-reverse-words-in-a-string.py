class Solution:
    def reverseWords(self, s: str) -> str:
        n=[]
        p=[]
        words=s.split()
        for i in words:
            n.append(i)
        for i in n:
            if(i==" "):
                continue
            else:
                p.append(i)
        p.reverse()
        return " ".join(p)
        