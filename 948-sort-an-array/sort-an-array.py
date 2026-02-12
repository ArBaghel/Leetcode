class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Bubble Sort
        # for i in range(len(nums)):
        #     for j in range (len(nums)-1):
        #         if nums[j]>=nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # return nums  
        #return sorted(nums)
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        l=self.sortArray(nums[:mid])
        r=self.sortArray(nums[mid:])
        return self.merge(l,r)
    def merge(self,l,r):
        ans=[]
        i=j=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                ans.append(l[i])
                i+=1
            else :
                ans.append(r[j])
                j+=1
        ans.extend(l[i:])
        ans.extend(r[j:])
        return ans

        

