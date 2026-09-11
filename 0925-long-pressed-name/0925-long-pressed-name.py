class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l=0
        r=0
        while(r<len(typed) and l<len(name)):
            if(name[l]==typed[r]):
                l=l+1
                r=r+1
            elif(r>0 and typed[r]==typed[r-1]):
                r=r+1
            else:
                return False
        if(len(name)>len(typed)):
            return False
        if(l<len(name)):
            return False
        while(r<len(typed)):
            if(typed[r]!=typed[r-1]):
                return False
            r=r+1
        return True
        