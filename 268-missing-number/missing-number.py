class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        Total_sum=n*(n+1)//2
        sum1=sum(nums)
        return Total_sum-sum1