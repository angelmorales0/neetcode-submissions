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
        
        def cycles(node, prev):
            if node in cycle:
                return False
            
            cycle.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not cycles(neighbor, node):
                    return False
            return True  #NO CYCLE 



        return cycles(0,-1) and n == len(cycle)