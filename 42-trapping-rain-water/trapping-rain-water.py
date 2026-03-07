class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        leftMax,rightMax=height[i],height[j]
        water=0
        while i<=j:
            if leftMax<=rightMax:
                leftMax=max(leftMax,height[i])
                water+=leftMax-height[i]
                i+=1
               
            elif rightMax<=leftMax:
                rightMax=max(rightMax,height[j])
                water+=rightMax-height[j]
                j-=1
               
        return water