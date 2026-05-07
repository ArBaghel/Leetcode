class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb=self.Lower(nums,target)
        ub=self.Upper(nums,target)
        if lb==ub: return [-1,-1]
        else:return [lb,ub-1]
    def Upper(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid
            else:
                l=mid+1
        return l
    def Lower(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l