class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #unidrected graph with n nodes same node structure
        #

        #step 1 create our graph 
        #graph can be represented as an adjancey list 

        # from there we need to have a dfs function that iterates through everything, 
        #from problem wording I dont htink we would need to account for loops 

        #go through every node and if not in visited run dfs on it, return total dfs calls


        adj = {node:[] for node in range(n)}

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visited = set()

        def dfs(prev,node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                dfs(node,neighbor)
            return 
        ret = 0
        for node in range(n):
            if node not in visited:
                dfs(-1,node)
                ret +=1
        return ret