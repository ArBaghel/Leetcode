class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        strs.sort()
        f,l=strs[0],strs[-1]
        i=0
        while i<len(f) and i<len(l) and f[i]==l[i]:
            i+=1
        return f[:i]