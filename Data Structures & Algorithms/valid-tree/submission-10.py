class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #nodes are from 0 -> n-1
        #list of edges -> Undirected goes both ways 

        #constructs a valid tree what makes up a valid tree?
        #must have n-1 edges 
        #all nodes must be reachable\
        #no cycles 
        
        #first check
        #what should I return if empty edges?

        if len(edges) != n-1:
            return False 
        
        #make an adjancery list
        adj = {node:[] for node in range(n)}
        for nodes in edges:
            adj[nodes[0]].append(nodes[1])
            adj[nodes[1]].append(nodes[0])
          

        #run dfs to iterate thru this list and see of a;; mpdes are reachable 
        visited = set()
        def dfs(prev, node): # goes through and checks for cycles 
            if adj[node] == []:
                visited.add(node)
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(node, neighbor):
                    return False
            return True



        if not dfs(-1,0):
            return False 
        if len(visited) == n:
            return True
        return False

          #visited = set() -> allow scycle detection 
            #dfs(node):

                #return true if you have no nodes to connect to 
                #return false if node is seen (cycle)
                #return true if every node is eventually connected to a no dep else  false 

