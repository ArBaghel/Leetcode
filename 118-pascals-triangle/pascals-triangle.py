class Solution:
    def generate(self, n: int) -> list[list[int]]:
        tri=[]
        for i in range (n):
            row=[1]*(i+1)
            for j in range (1,i):
                row[j]=tri[i-1][j-1]+tri[i-1][j]
            tri.append(row)
        return tri