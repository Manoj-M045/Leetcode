class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        n=[]
        for i in words[:k]:
            n.append(i)
        return " ".join(n)

            
        