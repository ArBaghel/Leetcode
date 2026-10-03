class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.merge(nums)
    def merge(self,nums):
        if len(nums)<=1:return nums
        res=[]
        mid=len(nums)//2
        l=self.merge(nums[:mid])
        r=self.merge(nums[mid:])
        while l and r:
            res.append(l.pop(0) if l[0]<r[0] else r.pop(0))
        return res+l+r

        