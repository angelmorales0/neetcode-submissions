class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #idea = traverse islands dfs and count them seen skip those if needed upon iteration return count of dfs calls 
        ret = 0
        seen = set()

        def traverse(r,c):
            if r < 0 or c <0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in seen or grid[r][c] == "0":
                return 
            seen.add ((r,c))
            for row,col in directions:
                traverse(r+row,c+col)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    ret += 1
                    traverse(r,c)
        print(seen)
        return ret
