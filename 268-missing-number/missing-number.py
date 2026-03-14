class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums :
        #         return i
        miss=len(nums)  
        for index,i in enumerate(nums):
            miss^=index^i
        return miss
            