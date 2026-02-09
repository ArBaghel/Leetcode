class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        c=0
        while i>=0 and s[i]!=" ":
                i-=1
                c+=1
                if i>=0 and s[i]==" ":
                    break
        return c
        