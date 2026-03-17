class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        num=[]
        for i in range (len(nums)):
            sum1+=nums[i]
            num.append(sum1)
        return num