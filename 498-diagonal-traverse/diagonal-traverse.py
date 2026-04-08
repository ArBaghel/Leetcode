class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
        ans=[]
        r=c=0
        d=1
        for _ in range (m*n):
            ans.append(mat[r][c])

            if d==1:
                if c==n-1:
                    d=-1
                    r+=1
                elif r==0:
                    c+=1
                    d=-1
                else:
                    r-=1
                    c+=1

            else:
                if r==m-1:
                    c+=1
                    d=1
                elif c==0:
                    r+=1
                    d=1
                else:
                    r+=1
                    c-=1
        return ans

        

        