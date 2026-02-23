class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = 1
        return False