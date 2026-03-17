class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=0
        for i in range (len(nums)):
            if nums[i] & 1 == 0:
                nums[s],nums[i]=nums[i],nums[s]
                s+=1
        return nums


        