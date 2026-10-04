class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [list(r) for r in zip(*matrix)]
        