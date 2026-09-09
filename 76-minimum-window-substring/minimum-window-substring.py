class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t={}
        for c in t:
            freq_t[c]=freq_t.get(c,0)+1

        freq_s={}
        l=0
        curlen=0
        res=len(s)+1
        left=right=0
        for r,c in enumerate(s):
            freq_s[c]=freq_s.get(c,0)+1
            if c in freq_t and freq_s[c]==freq_t[c]:
                curlen+=1

            while curlen==len(freq_t):
                if r-l+1<res:
                    res=r-l+1
                    left=l
                    right=r
                freq_s[s[l]]-=1
                if s[l] in freq_t and freq_s[s[l]]<freq_t[s[l]]:
                    curlen-=1
                l+=1
        return "" if res==len(s)+1 else s[left:right+1]
        