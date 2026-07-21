class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while l < r:
            area=min(height[l],height[r])*(r-l)
            if height[r]<height[l]:
                r-=1
            else :l+=1
            maxarea=max(maxarea,area)
        return maxarea
