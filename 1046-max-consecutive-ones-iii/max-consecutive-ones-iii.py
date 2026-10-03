class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=zeroes=mf=0
        for r in range (len(nums)):
            if nums[r]==0:
                zeroes+=1
            while zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            mf=max(mf,r-l+1)
        return mf
