class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen,l,maxi={},0,0
        for r, i in enumerate(s):
            if i in seen and seen[i]>=l:
                l=seen[i]+1
            seen[i]=r
            maxi=max(maxi,r-l+1)
        return maxi
        