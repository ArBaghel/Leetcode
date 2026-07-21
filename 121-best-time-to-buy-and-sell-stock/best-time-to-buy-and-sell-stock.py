class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            cur=prices[i]-min_price 
            p=max(p,cur)
            min_price=min(prices[i],min_price)
        return p
        