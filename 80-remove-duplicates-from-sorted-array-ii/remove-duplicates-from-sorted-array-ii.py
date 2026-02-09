class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        s=1
        for i in range (2,n):
           if nums[i]!=nums[s-1]:
                s+=1
                nums[s]=nums[i]
            
        return s+1