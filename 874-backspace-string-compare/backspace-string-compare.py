class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for c in list(s):
            if c!='#':
                s1.append(c)
            elif len(s1)>0:
                s1.pop()
        for c in list(t):
            if c!='#':
                s2.append(c)
            elif len(s2)>0:
                s2.pop()
        return s1==s2