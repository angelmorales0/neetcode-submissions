class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #make a list for cols where pacific can flow
        #make one for atlantic and see what valeus map 
        directions = [ [-1,0],[1,0],[0,1],[0,-1]]
        rows = len(heights)
        cols = len(heights[0])
        atl = set()
        pac = set()

        def dfs(r,c,listt,prev_h):
            if r < 0 or c<0 or r >= rows or c >= cols or (r,c) in listt or prev_h > heights[r][c]:
                return 
            listt.add((r,c))
            for direction in directions:
                dfs(r+direction[0],c+direction[1],listt,heights[r][c] ) 

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range (rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        ret = []
        for v1 in atl:
            for v2 in pac:
                if v1==v2:
                    ret.append([v1[0],v1[1]])
        return ret



       