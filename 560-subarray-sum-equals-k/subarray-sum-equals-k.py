class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=s=0
        f={0:1}
        for i in nums:
            s+=i
            if s-k in f:
                c+=f[s-k]
            f[s]=f.get(s,0)+1
        return c
        