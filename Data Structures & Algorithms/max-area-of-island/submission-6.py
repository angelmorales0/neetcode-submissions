class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sett  = set()
        rowmax = len(grid)
        cmax = len(grid[0])
        res = []
        index = 0

        maxArea = 0

        def backtrack(r, c ):
            nonlocal maxArea
            
            if r < 0 or r >= rowmax:
                return 
            if c < 0 or c >= cmax:
                return 

            if tuple([r, c]) in sett or grid[r][c] == 0:
                return 
            
            sett.add(tuple([r, c]))  
            res.append([r,c])        
          
            backtrack(r-1, c)
            backtrack(r+1, c)
            backtrack(r, c-1)
            backtrack(r, c+1)



        for i in range(rowmax):
            for j in range (cmax):
                if grid[i][j] == 1:
                    backtrack(i, j)
                    print(res)
                    maxArea = max(maxArea, len(res))
                    res.clear()
                    
        return maxArea
        
            

        