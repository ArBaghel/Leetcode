class Solution:
    def reverseWords(self, s: str) -> str:
        # s=(s.strip()).split()
        # s.reverse()
        # return " ".join(s)
        n=len(s)
        i=n-1
        ans=[]
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            j=i
            while i>=0 and s[i]!=" ":
                i-=1
            ans .append(s[i+1:j+1])
        return " ".join(ans)