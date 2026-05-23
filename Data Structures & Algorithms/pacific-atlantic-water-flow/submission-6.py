class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        row, col = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r < 0 or r >= row or
                c < 0 or c >= col or
                heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
        
        for i in range(row):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Pacific Ocean (left edge)
            dfs(i, col - 1, atlantic_reachable, heights[i][col - 1])  # Atlantic Ocean (right edge)
        
        for j in range(col):
            dfs(0, j, pacific_reachable, heights[0][j])  # Pacific Ocean (top edge)
            dfs(row - 1, j, atlantic_reachable, heights[row - 1][j])  # Atlantic Ocean (bottom edge)
        
        return list(pacific_reachable & atlantic_reachable)