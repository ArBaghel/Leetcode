class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c=0
        can=None
        for num in nums:
            if c==0:
                can=num
            c+=(1 if can==num else -1)
        return can
        