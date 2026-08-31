class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # for i in range (len(nums)):
        #     total=nums[i]
        #     for j in range(i+1,len(nums)):
        #         total+=nums[j]
        #         if total%k==0:return True
        # return False
        dic={0:-1}
        runsum=0
        for i in range (len(nums)):
            runsum+=nums[i]
            rem=runsum%k
            if rem not in dic:
                dic[rem]=i
            elif i-dic[rem]>1:
                return True
        return False

            
        