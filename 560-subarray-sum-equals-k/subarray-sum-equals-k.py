class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        csum=0
        f={0:1}
        for i in nums:
            csum+=i
            if csum-k in f:
                count+=f[csum-k]
            f[csum]=f.get(csum,0)+1
        return count
        