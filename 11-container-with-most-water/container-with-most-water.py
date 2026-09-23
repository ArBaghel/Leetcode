class Solution:
    def maxArea(self, h: list[int]) -> int:
        l,r,=0,len(h)-1
        maxa=0
        while l<r:
            area=min(h[l],h[r])*(r-l)
            if h[l]>h[r]:
                r-=1
            else:l+=1
            maxa=max(area,maxa)
        return maxa

        