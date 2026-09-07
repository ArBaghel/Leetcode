class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        p_count=[0]*26
        w_count=[0]*26

        for ch in p:
            idx=ord(ch)-ord('a')
            p_count[idx]+=1

        l=0
        res=[]

        for r in range (len(s)):
            idx=ord(s[r])-ord('a')
            w_count[idx]+=1
        
            if r-l+1==len(p):
                if w_count==p_count:
                    res.append(l)
                idx=ord(s[l])-ord('a')
                w_count[idx]-=1
                l+=1
        return res
        