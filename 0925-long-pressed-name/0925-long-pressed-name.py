class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1=0
        ptr2=0
        if(len(typed)<=len(name)):
            if(name!=typed):
                return False       
        while(ptr1<len(name)and ptr2<len(typed)):
            if(name[ptr1]==typed[ptr2]):
                ptr1+=1
                ptr2+=1
            else:
                if(ptr2>0 and typed[ptr2]==typed[ptr2-1]):
                    ptr2+=1
                else:
                    return False
        if(ptr1<len(name)):
            return False
        while(ptr2<len(typed)):
            if(name[-1]!=typed[ptr2]):
                return False
            ptr2+=1
        return True
        