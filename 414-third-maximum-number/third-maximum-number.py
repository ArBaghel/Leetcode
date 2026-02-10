class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        n=len(nums)
        if n<3:
            return nums[-1]
        else:
            return nums[-3]
         