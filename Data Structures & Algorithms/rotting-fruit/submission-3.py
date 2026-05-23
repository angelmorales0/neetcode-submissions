class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0

        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = set()

        for i in range( row):
            for j in range (col):
                if grid[i][j] == 2:
                    q.append([i, j])
        while q:
            fruits_changed = False
            for i in range(len(q)):# does it for all children at once.
                
                rot = q.popleft()
    
                r = rot[0]
                c = rot[1] 
                if r< 0 or r>= row or c< 0 or c>= col:
                    continue

                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append([r-1, c])
                    fruits_changed = True
                if r+1 < row  and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append([r+1, c])
                    fruits_changed = True
                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append([r, c-1])
                    fruits_changed = True
                if c+1 < col  and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append([r, c+1])
                    fruits_changed = True
                
            if fruits_changed:
                time += 1
            
          


        for row in grid:
            if 1 in row:
                return -1
        return time
        