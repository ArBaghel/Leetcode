class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
        res=[]
        for d in range( m+n-1 ):
            diag = []
            r = max(0,d-n+1)
            c = d - r
            while r < m and c >= 0:
                diag.append ( mat [r] [c] )
                r,c = r + 1,c - 1
            res.extend ( diag [ ::-1 ] if d % 2 == 0 else diag )
        return res
        # m, n = len(mat), len(mat[0])
        # res = []
        # for d in range(m + n - 1):
        #     tmp = [mat[i][d - i] for i in range(max(0, d - n + 1), min(m, d + 1))]
        #     res.extend(tmp[::-1] if d % 2 == 0 else tmp)
        # return res
      
        

        