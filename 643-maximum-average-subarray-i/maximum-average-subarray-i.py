class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=curr=sum(nums[:k])
        for i in range (k,len(nums)):
            curr += nums[i]-nums[i-k] 
            maxi=max(maxi,curr)
        return maxi/k