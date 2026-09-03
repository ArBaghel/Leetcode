class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        ws=0
        ans=float('-inf')
        l=0
        for r in range (len(arr)):
            ws+=arr[r]
            if r-l+1==k:
                ans=max(ans,ws/k)
                ws-=arr[l]
                l+=1
        return ans