class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        sett = set()
        rowmax = len(grid)
        cmax = len(grid[0])

        print(rowmax, cmax)
        def backtrack(r,c):

            if grid[r][c] == "0" or tuple([r, c]) in sett:
                return
            sett.add(tuple([r, c]))

            

            if c-1 >= 0 and grid[r][c-1] and grid[r][c-1] == "1":
                backtrack(r,c-1)
                sett.add(tuple([r, c-1]))

            if c+1 < cmax and grid[r][c+1] and grid[r][c+1] == "1":
                backtrack(r,c+1)
                sett.add(tuple([r, c+1]))

            if r-1 >= 0 and  grid[r-1][c] and grid[r-1][c] == "1" :
                backtrack(r-1,c)
                sett.add(tuple([r-1, c]))

            if r+1 < rowmax and grid[r+1][c] and grid[r+1][c] == "1":
                backtrack(r+1,c)
                sett.add(tuple([r+1, c]))
            
            
            return 

        for r in range(rowmax):

            for c in range(cmax):
                
                if tuple([r, c]) not in sett and grid[r][c] == "1":
                
                    backtrack(r,c)
                    ret += 1
                    

        return ret
            
                

        
        