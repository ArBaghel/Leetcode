class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p,minp=0,prices[0]
        for i in range (1,len(prices)):
            cur=prices[i]-minp
            minp=min(minp,prices[i])
            p=max(p,cur)
        return p        