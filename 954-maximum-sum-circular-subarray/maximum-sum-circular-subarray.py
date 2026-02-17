class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=nums[0]
        for i in range(len(nums)):
            curr_sum+=nums[i]
            max_sum=max(curr_sum,max_sum)
            if  curr_sum<0:
                curr_sum=0
        curr_sum=0
        min_sum=nums[0]
        for i in range(len(nums)):
            curr_sum+=nums[i]
            min_sum=min(curr_sum,min_sum)
            if  curr_sum>0:
                curr_sum=0
        totalSum=sum(nums)
        
        if max_sum<0:
            return max_sum
        return max(max_sum,totalSum-min_sum)
        