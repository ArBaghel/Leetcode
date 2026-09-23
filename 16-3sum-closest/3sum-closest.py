class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closesum=float('inf')
        for i in range (len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if abs(closesum-target) > abs(summ-target):
                    closesum=summ
                    
                elif summ<target:
                    j+=1
                elif summ>target:
                    k-=1
                else:
                    return summ
        return closesum
        