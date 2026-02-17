class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=[nums[0]]
        rightSum=[nums[-1]]
        for i in range (1,len(nums)):
            leftSum.append(nums[i]+leftSum[i-1])
        for i in range(len(nums)-2,-1,-1):
            rightSum.insert(0,nums[i]+rightSum[0])
        for i in range (len(nums)):
            if leftSum[i]==rightSum[i]:
                return i
        return -1