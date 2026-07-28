class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(mat),len(mat[0])
        r,c=[],[]
        for i in range(m):
            for j in range(n):
                if mat [i][j] == 0:
                    r.append(i)
                    c.append(j)
        for i in range (m):
            for j in range(n):
                if i in r or j in c:
                    mat[i][j]=0

