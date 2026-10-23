class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb,ub=self.lowerBound(target,nums),self.upperBound(target,nums)
        if lb==ub:return [-1,-1]
        else :return [lb,ub-1]
    def upperBound(self,target,nums):
        l,r=0,len(nums)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>target:
                r=mid
            else:l=mid+1
        return l
    def lowerBound(self,target,nums):
        l,r=0,len(nums)
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>=target:
                r=mid
            else:l=mid+1
        return l
        