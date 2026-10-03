class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=maxf=res=0
        f={}
        for r,ch in enumerate(s):
            f[ch]=f.get(ch,0)+1
            maxf=max(f[ch],maxf)
            if (r-l+1)-maxf>k:
                f[s[l]]-=1
                l+=1
            res=max(maxf,r-l+1)
        return res


        