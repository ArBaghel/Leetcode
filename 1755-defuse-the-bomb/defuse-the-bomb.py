class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0: return [0]*len(code)
        return [sum(code[(i+j)% len(code)] for j in (range(1,k+1) if k>0 else range(k,0))) for i in range(len(code))]