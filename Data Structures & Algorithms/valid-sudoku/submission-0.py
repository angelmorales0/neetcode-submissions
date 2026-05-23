
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking rows and columns
        for i in range(9):
            row_seen, col_seen = set(), set()
            for j in range(9):
                # Row check
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])
                
                # Column check
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])
        
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
