class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb=self.lower(nums,target)
        ub=self.upper(nums,target)
        if lb==ub:return [-1,-1]
        else:return [lb,ub-1]
    def upper(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid
            else:l=mid+1
        return l

    def lower(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid
            else:l=mid+1
        return l
    
    