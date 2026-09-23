import itertools
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        We are given a rectangular island / grid where the heights represent the hieght above sea level 
        pacific = top and left side, atlanitc = bottom and irhgt side 
        
        Find cells 

        We have an input heights 
        Want to find all levels water can flow to from pacific and atlandic ocean 
        and return all cells tht contain both oceans 


        idea = make pacific set, and atlantic set and reutnr both  maybe thru a hashmap ???

        """
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        cols = len(heights[0])
        rows = len(heights)

        pacificOcean = set((0,col) for col in range(len(heights[0])))
        pacificOcean.update((row,0) for row in range(len(heights)))        
        atlanticOcean = set((rows-1,col) for col in range(len(heights[0])))
        atlanticOcean.update((row,cols-1) for row in range(len(heights)))

        def dfs(x,y,prevHeight,visited):
            if (x,y) in visited:
                return
            
            if not (0 <= x < len(heights)) or not (0 <= y < len(heights[0])): #if not in bounds ret
                return
            if not heights[x][y] >= prevHeight:
                return 
            
            visited.add((x,y))
     
            for xOff, yOff in directions:
                dfs(x+xOff, y + yOff, heights[x][y],visited)
        
        pacificSet = set()
        atlanticSet = set()
        for row, col in itertools.chain(pacificOcean):
                dfs(row,col,heights[row][col],pacificSet)
        for row, col in itertools.chain(atlanticOcean):
            dfs(row,col,heights[row][col],atlanticSet)
        
        
        return list(pacificSet & atlanticSet)

            
            

