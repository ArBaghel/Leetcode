class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k=0
        # for i in range (len(nums)):
        #     if nums[i] != val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k
        fil= [i for i in nums if i != val]
        nums[:len(fil)]=fil
        return len(fil)