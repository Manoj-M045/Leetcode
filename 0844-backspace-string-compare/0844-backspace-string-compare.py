class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=len(s)-1
        t1=len(t)-1
        ss=0
        st=0
        while(s1>0 or t1>=0):
            while(s1>=0):
                if(s[s1]=='#'):
                    ss+=1
                    s1-=1
                elif(ss>0 and s[s1]!='#'):
                    ss-=1
                    s1-=1
                else:
                    break
            while(t1>=0):
                if(t[t1]=='#'):
                    st+=1
                    t1-=1
                elif(st>0 and t[t1]!="#"):
                    st-=1
                    t1-=1
                else:
                    break
            if(s1>=0 and t1>=0):
                if(s[s1]!=t[t1]):
                    return False
            elif(s1>=0 or t1>=0):
                return False
            s1-=1
            t1-=1
        return s1==t1
        

        
        

        