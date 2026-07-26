class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans=[]
        cs=float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:continue
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if abs(cs-target)>abs(s-target):
                    cs=s
                elif s>target:
                    k-=1
                elif s<target:
                    j+=1
                
                else:return s
        return cs