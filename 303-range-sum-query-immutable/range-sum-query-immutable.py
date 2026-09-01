class NumArray:

    def __init__(self, nums: List[int]):
        self.preffixsum=[0]
        for i in nums:
            self.preffixsum.append(self.preffixsum[-1]+i)

    def sumRange(self, left: int, right: int) -> int:
        return self.preffixsum[right+1]-self.preffixsum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)