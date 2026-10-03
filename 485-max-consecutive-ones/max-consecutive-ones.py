class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxc=0
        c=0
        for i in range(len(nums)):
            if nums[i]<1:
                c=0
            else:c+=1
            maxc=max(c,maxc)
        return maxc