class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        s='0'+''.join(map(str,fb))+'0'
        return sum((len(x)-1)//2 for x in s.split('1'))>=n
    
        
        