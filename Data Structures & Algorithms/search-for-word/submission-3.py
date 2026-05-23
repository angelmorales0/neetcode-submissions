class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxrow = len(board)
        maxcolumn = len(board[0])
        sett = set() # to avoid reusing 
        
        def dfs(row, column, i):
            if i == len(word):
                return True

            if row < 0 or column < 0 or row >= maxrow or column >= maxcolumn or board[row][column] != word[i] or tuple([row,column]) in sett:
                return False
            sett.add(tuple([row,column]))

            ret = dfs(row-1, column, i +1) or dfs(row+1, column, i+1) or dfs(row, column-1, i +1) or dfs(row, column+1, i+1)

            sett.remove(tuple([row,column]))
            return ret

        for row in range(maxrow):
            for column in range(maxcolumn):
                if board[row][column] == word[0]:
                    if dfs(row,column,0):
                        return True
        return False

                
               



