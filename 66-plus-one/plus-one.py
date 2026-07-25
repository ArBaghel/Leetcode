class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       nums=int(''.join(map(str,digits)))
       nums+=1
       return[int(d) for d in str(nums)]
        