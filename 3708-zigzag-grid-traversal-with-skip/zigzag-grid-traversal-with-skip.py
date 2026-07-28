class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res=[]
        for i in range (len(grid)):
            r=grid[i] if i%2 ==0 else grid[i][::-1]
            res.extend(r)
        return res[::2]
        