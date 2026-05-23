class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        

        def ofind(r,c):
            if r< 0 or r == len(board):
                return 
            if c < 0 or c == len(board[0]):
                return 
            if board[r][c] != 'O':
                return 
            board[r][c] = 'T' # change all un capturable targets to T WE know this is uncapturable as it is on the edge, an O is only
            #uncapturable if connected to an edge o,
            ofind(r-1,c)
            ofind(r+1,c)
            ofind(r,c-1)
            ofind(r,c+1)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and( i in [0, row-1] or j in [0, col-1]):
                    ofind(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        
                    
                    
                    


                    
                
            


        