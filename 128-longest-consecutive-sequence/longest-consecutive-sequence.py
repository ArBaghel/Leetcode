class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        maxc=c=1
        nums.sort()
        for i in range (len(nums)-1):
            if nums[i+1]==nums[i]+1:
                c+=1
                maxc=max(maxc,c)
            elif nums[i+1]!=nums[i]:
                c=1
        return maxc
        