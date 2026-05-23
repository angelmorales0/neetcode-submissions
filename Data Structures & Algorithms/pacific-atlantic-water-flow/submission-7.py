class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])
        atl = set()
        pac = set()
        ret = []


        def dfs(r, c, sett, prevHeight):
            
            if r < 0 or c < 0:
                return #out of bounds
            if r >= row or c>= col:
                return 

            if heights[r][c] < prevHeight:
                return #water cant flow 
                
            if (r, c) in sett:
                return 

            sett.add((r, c))
            dfs(r-1, c, sett, heights[r][c])
            dfs(r+1, c, sett, heights[r][c])
            dfs(r, c+1, sett,heights[r][c])
            dfs(r, c-1,sett, heights[r][c])

        for i in range(row):
            dfs(i, 0, pac, heights[i][0])  # Left edge
            dfs(i, col - 1, atl, heights[i][col - 1])  # Right edge
        for j in range(col):
            dfs(0, j, pac, heights[0][j])  # Top edge
            dfs(row - 1, j, atl, heights[row - 1][j])  # Bottom edge

        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    ret.append([r, c])



        return ret

    