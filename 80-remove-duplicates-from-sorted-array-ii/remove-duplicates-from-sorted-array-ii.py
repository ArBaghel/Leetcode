class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=1
        for i in range (2,len(nums)):
            if nums[i] != nums[s-1]:
                s+=1
            nums[s]=nums[i]
        return s+1
        