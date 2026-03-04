class Solution:
    def lowerBound(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l
    def UpperBound(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.lowerBound(nums,target)
        ub=self.UpperBound(nums,target)
        return [-1,-1] if lb==ub else [lb,ub-1]
