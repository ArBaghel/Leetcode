class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l,r=0,row*col-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid//col][mid%col]==target:
                return True
            elif matrix[mid//col][mid%col] > target:
                r=mid-1
            else :
                l=mid+1
        return False
        