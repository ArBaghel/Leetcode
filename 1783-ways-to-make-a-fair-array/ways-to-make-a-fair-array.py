class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_s=sum(nums[::2])
        odd_s=sum(nums[1::2])
        prefix_e=prefix_o=0
        count=0
        for i , num in enumerate(nums):
            if i%2==0:
                even_s-=num
                if prefix_e+odd_s==prefix_o+even_s:
                    count+=1
                prefix_e+=num
            else:
                odd_s-=num    
                if prefix_e+odd_s==prefix_o+even_s:
                    count+=1
                prefix_o+=num
        return count