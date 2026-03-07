class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        leftMax,rightMax=height[i],height[j]
        water=0
        while i<j:
            if leftMax<=rightMax:
                i+=1
                leftMax=max(leftMax,height[i])
                water+=leftMax-height[i]
                
               
            elif rightMax<=leftMax:
                j-=1
                rightMax=max(rightMax,height[j])
                water+=rightMax-height[j]
                
               
        return water