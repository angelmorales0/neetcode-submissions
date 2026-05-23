class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #first we need to iterate thru all things and add 1 to permiter if it is water OR OOB
        #
        row_max = len(grid)
        col_max = len(grid[0])
        perim = 0
        seen = set()

        def dfs(row,col):
            nonlocal perim

            if row <0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0 or (row,col) in seen:
                return 

            seen.add( (row,col))

        
            if row+1 >= row_max or grid[row+1][col] == 0:
                perim +=1
         
                dfs(row+1,col)
            if row-1 <0 or grid[row-1][col] == 0:
                perim +=1
                dfs(row-1,col)
            if col+1 >= col_max or grid[row][col+1] == 0:
                perim +=1
                dfs(row,col+1)
            if col-1 <0 or grid[row][col-1] == 0:
                perim +=1
                dfs(row,col-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen: 
                    dfs(r,c)
                    print("once")
                    print(seen)

                
        return perim 