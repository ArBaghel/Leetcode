class Solution:
    def rob(self, nums: List[int]) -> int:
        p1=p2=0
        for i in nums:
            p1,p2=max(p2+i,p1),p1
        return p1
        

        