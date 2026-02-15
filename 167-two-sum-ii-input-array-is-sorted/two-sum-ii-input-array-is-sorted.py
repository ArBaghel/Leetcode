class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
        #  dict1={}
        # for i in range (len(numbers)):
        #     rem=target-numbers[i]
        #     if rem in dict1:
        #         return [dict1[rem]+1,i+1]

        #     dict1[numbers[i]]=i    