class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        """
        Do not return anything, modify matrix in-place instead.
        """
       # matrix[:]=zip(*matrix[::-1])
        
        for i in range(n):
            for j in range (i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for r in matrix:
            r.reverse()