class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=[]
        for nums in accounts:
            sum1=0
            for i in nums:
                sum1+=i
            maxsum.append(sum1)
        return max(maxsum)


        #return max(sum(nums) for nums in accounts)