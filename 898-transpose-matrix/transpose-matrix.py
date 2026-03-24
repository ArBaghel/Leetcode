class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # m=len(matrix)
        # n=len(matrix[0])
        # tmat=[[0]*m for _ in range (n)]
        # for row in range (n):
        #     for col in range(m):
        #         tmat[row][col]=matrix[col][row]
        # return tmat
        return[[matrix[j][i] for j in range (len(matrix))] for i in range (len(matrix[0]))]

        