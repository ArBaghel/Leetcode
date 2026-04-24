class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count,ans=[0]*101,0
        for i in nums:
            ans+=count[i]
            count[i]+=1
        return ans