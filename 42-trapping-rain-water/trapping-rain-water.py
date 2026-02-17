class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        leftMax,rightMax=height[0],height[j]
        water=0
        while i<j:
            if leftMax<=rightMax:
                water+=leftMax-height[i]
                i+=1
                leftMax=max(leftMax,height[i])
            elif rightMax<=leftMax:
                water+=rightMax-height[j]
                j-=1
                rightMax=max(rightMax,height[j])
        return water
