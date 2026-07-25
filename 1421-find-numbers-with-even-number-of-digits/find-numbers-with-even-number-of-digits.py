class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            digitcount=0
            while i>0:
                i//=10
                digitcount+=1
            if digitcount & 1==0:
                c+=1
        return c
       
        