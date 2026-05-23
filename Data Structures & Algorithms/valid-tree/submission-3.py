class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #A tree is considered unvalid if it has a cycle 

        
        cycle = set()
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2) #index i has its neighbors 
            adj[n2].append(n1)
    
        def dfs(node,prev):
            if node in cycle:
                return False
            
            cycle.add(node)
            
            for nextt in adj[node]:
                if nextt == prev:
                    continue
                if not dfs (nextt, node):
                    return False 
            return True

        if not dfs(0,-1):
            return False
        if n != len(cycle):
            return False
        return True