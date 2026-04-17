class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        x, y = len(mat), len(mat[0])
        if x * y != r * c:
            return mat
        flat = sum(mat, [])
        it = iter(flat)
        return [list(row) for row in zip(*[it]*c)]