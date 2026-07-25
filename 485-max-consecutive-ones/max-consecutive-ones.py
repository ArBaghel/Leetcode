class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maxcount=0
        for i in range (len(nums)):

            if nums[i] <1:
                c=0
            else: 
                c+=1
                maxcount=max(c,maxcount)
        return maxcount

        