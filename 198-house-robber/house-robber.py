from functools import lru_cache
class Solution:
   def rob(self, nums: List[int]) -> int:
    n = len(nums)
    @lru_cache(None)
    def solve(i):
        if i>=n:return 0
        return max(nums[i]+solve(i+2),solve(i+1))
    return solve(0)
   