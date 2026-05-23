class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #return true if owrd is present 
        #for a word to be considered presengt it must be possible to get it via dfs 

        #Loop through every start index as the start and and run dfs in all directions until you get word
        #then ret true if found else ret false
        #O(M*N)

        #for r in range row:
            #for c in range col 
                #run dfs (curr letter,r,c)
        
        #dfs(currentWord,r,c)
            #if currentWord == word:
                #return True 
            #if OOB :
                #return False 
            #If any char in currentWord doesnt match target: #alr impossible 
                #ret false
            #for d in directions:
                # if dfs (currWord + grid[r][c], r+ d[0], c + d[1])
                   # return True
         #   return False

        directions = [ [-1,0], [1,0], [0,-1], [0,1]]
        rowMax = len(board)
        colMax = len(board[0])
        seen = set()
        def dfs(currentWord, r,c): # right now we dont account for backtracking -> Need to account
            if currentWord == word:
                return True
            if r< 0 or c <0 or r >= rowMax or c >= colMax or len(currentWord) > len(word) or (r,c) in seen:
                return False
            for i in range (len(currentWord)):
                if currentWord[i] != word[i]:
                    return False
            for d in directions:
                seen.add( (r,c) )
                if dfs (currentWord + board[r][c],r+d[0], c+d[1]):
                    return True
                seen.remove((r,c))
            return False

        for r in range (rowMax):
            for c in range (colMax):
                if dfs("",r,c):
                    return True
        return False


        