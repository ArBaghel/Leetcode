class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0: return [0]*n
        # return [sum(code[(i+j)% len(code)] for j in (range(1,k+1) if k>0 else range(k,0))) for i in range(len(code))]
        res,ws=[],0
        if k>0:
            for i in range (1,k+1):
                ws+=code[i%n]
            res.append(ws)
            for i in range (1,n):
                ws+=code[(i+k)%n]-code[i]
                res.append(ws)
        else :
            k=-k
            for i in range (1,k+1):
                ws+=code[-i]
            res.append(ws)
            for  i in range(1,n):
                ws+=code[i-1]-code[(i-k-1)%n]
                res.append(ws)
        return res