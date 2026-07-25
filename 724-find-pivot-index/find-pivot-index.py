class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        r=totalsum
        l=0
        for i in range (len(nums)):
            r-=nums[i]
            if l==r:
                return i
            l+=nums[i]
        return -1
        
        