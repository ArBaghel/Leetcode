class Solution:
    def gethour(self,piles,mid):
        ans=0
        for pile in piles:
            ans+=(pile+mid-1)//mid
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            mid=(l+r)//2
            if self.gethour(piles,mid) > h:
                l=mid+1
            else:
                r=mid-1
        return l
        