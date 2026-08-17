class Solution:
    def capitalizeTitle(self, title: str) -> str:
        k=[]
        words=title.split()
        for i in words:
            if(len(i)>2):
               k.append(i.title())
            else:
                k.append(i.lower())
        return " ".join(k)
        