class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        s=sorted(map(str,nums),key=lambda x:x*10,reverse=True)
        s=''.join(s)
        return "0" if s[0]=="0" else s
        