class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        for i in prices:
            cur=i+min_price
            profit=max(profit,i-min_price)
            min_price=min(min_price,i)
        return profit
        