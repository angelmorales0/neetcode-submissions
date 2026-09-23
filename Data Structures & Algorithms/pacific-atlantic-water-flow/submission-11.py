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
        
        oceanFlow = defaultdict(set)
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        colCount = len(heights[0])
        rowCount = len(heights)

        pacificOcean = set((0,col) for col in range(len(heights[0])))
        pacificOcean.update((row,0) for row in range(len(heights)))
        
        atlanticOcean = set((rowCount-1,col) for col in range(len(heights[0])))
        atlanticOcean.update((row,colCount-1) for row in range(len(heights)))

        print(atlanticOcean)

        def dfs(x,y,prevHeight,origin,visited):
            if (x,y) in visited:
                return
            
            if not (0 <= x < len(heights)) or not (0 <= y < len(heights[0])):
                return
            if prevHeight < heights[x][y]:
                return 

            #IT  CAN FLOW HERE 

            if (x,y) in atlanticOcean:
                oceanFlow[origin].add('A')
                
            if (x,y) in pacificOcean:
                oceanFlow[origin].add('P')
            
            visited.add((x,y))
     
            for xOff, yOff in directions:
                dfs(x+xOff, y + yOff, heights[x][y], origin,visited)
        
        for row in range(rowCount):
            for col in range(colCount):
                dfs(row,col,heights[row][col],(row,col),set())
    
        
        ret = []
        for index, oceans in oceanFlow.items():
            if 'A' in oceans and 'P' in oceans:
                ret.append(index)
        return ret

            
            

