class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        maxlen=0
        csum=0
        for i , n in enumerate(nums):
            csum+=1 if n else -1
            if csum in d:
                maxlen=max(maxlen,i-d[csum])
            else:
                d[csum]=i
        return maxlen
        