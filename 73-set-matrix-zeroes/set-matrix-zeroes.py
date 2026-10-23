class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=[],[]
        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if i in r or j in c:
                    matrix[i][j]=0


        