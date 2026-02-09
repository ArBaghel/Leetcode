class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])

        total=m*n 
        ans=[] 
        count=0

        cols,rows=0,0
        colend,rowend=m-1,n-1

        while count < total :
            #rows , cols->colend
            for i in range(cols,colend+1):
                ans.append(matrix[rows][i])
                count+=1
            rows+=1
            if count==total:
                break
            #colend , rows->rowend
            for i in range(rows,rowend+1):
                ans.append(matrix[i][colend])
                count+=1
            colend-=1
            if count==total:
                break
            #rowend , colend->cols
            for i in range(colend,cols-1,-1):
                ans.append(matrix[rowend][i])
                count+=1
            rowend-=1
            if count==total:
                break
            #cols , rowend->rows
            for i in range(rowend,rows-1,-1):
                ans.append(matrix[i][cols])
                count+=1
            cols+=1
        return ans
