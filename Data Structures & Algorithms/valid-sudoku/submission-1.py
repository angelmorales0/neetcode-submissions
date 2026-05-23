
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = set()
        colSeen = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rowSeen:
                        return False
                    rowSeen.add(board[r][c])
                if board[c][r] != ".":
                    if board[c][r] in colSeen:
                        return False
                    colSeen.add(board[c][r])         
            rowSeen.clear()
            colSeen.clear()





        # Checking 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
        
        return True
