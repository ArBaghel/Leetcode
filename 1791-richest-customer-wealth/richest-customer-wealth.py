class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        s=0
        for num in accounts:
            s=sum(num)
            m=max(s,m)
        return m

        