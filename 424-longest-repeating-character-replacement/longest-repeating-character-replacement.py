class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=maxf=maxw=0
        freq={}
        for r in range(len(s)):
            ch=s[r]
            freq[ch]=freq.get(ch,0)+1
            maxf=max(maxf,freq[ch])

            while (r-l+1)-maxf>k:
                freq[s[l]]-=1
                l+=1
            maxw=max(maxw,r-l+1)
        return maxw
        