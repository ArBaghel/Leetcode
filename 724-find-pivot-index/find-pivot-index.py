class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        ls=0
        for i in range (len(nums)):
            rs=totalsum-ls-nums[i]
            if rs==ls:
                return i
            ls+=nums[i]
        return -1