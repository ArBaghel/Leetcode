class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for r in range (1,len(nums)):
            if nums[r]!=nums[i]:
                i+=1
                nums[i]=nums[r]
        return i+1       
        