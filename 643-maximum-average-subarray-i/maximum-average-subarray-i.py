class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # ws=0
        # ans=float('-inf')
        # l=0
        # for r in range (len(arr)):
        #     ws+=arr[r]
        #     if r-l+1==k:
        #         ans=max(ans,ws/k)
        #         ws-=arr[l]
        #         l+=1
        # return ans
        maxi=curr=sum(nums[:k])
        for i in range (k,len(nums)):
            curr += nums[i]-nums[i-k] 
            maxi=max(maxi,curr)
        return maxi/k