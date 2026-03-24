class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        total=m*n
        ans=[]
        c=0
        row,col=0,0
        rowe,cole=n-1,m-1
        while c < total:
            # row, col -> cole
            for i in range (col,cole+1):
                ans.append(matrix[row][i])
                c+=1
            row+=1
            if c==total:
                break
             # cole, row -> rowe
            for i in range (row,rowe+1):
                ans.append(matrix[i][cole])
                c+=1
            cole -= 1
            if c==total:
                break
             # rowe, cole -> col
            for i in range (cole,col-1,-1):
                ans.append(matrix[rowe][i])
                c+=1
            rowe-=1
            if c==total:
                break
            # cole , rowe -> row
            for i in range( rowe, row-1,-1):
                ans.append(matrix[i][col])
                c+=1
            col+=1
        return ans

