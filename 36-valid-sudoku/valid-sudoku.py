class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #validate row
        for i in range (9):
            s=set()
            for j in range(9):
                item=board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        #validate cols
        for i in range (9):
            s=set()
            for j in range(9):
                item=board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        #valid sub-box
        for br in range(0,9,3):
            for bc in range(0,9,3):
                s=set()
                for i in range(3):
                    for j in range (3):
                        item=board[br+i][bc+j]
                        if item in s:return False
                        elif item != '.':
                            s.add(item)
        return True