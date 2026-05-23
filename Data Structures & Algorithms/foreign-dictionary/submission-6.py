class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #have a hashmap showing deps -> can have multi so itll be an array 
        graph = {c:set() for w in words for c in w} #gets us a set with every cahr 

        for i in range(len(words)-1): #to compare pairs 
            w1 = words[i]
            w2 = words[i+1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # this is the given basecase for returning a bad input
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        visited = {} #this is used to track if we are in a cycle (since we cant run topological sort on a cycle)
        ret = []

        def dfs(c): #this is the topoligcal sort part of the algo
            if c in visited:
                return visited[c] 
            visited[c] = True
            for nextNode in graph[c]:
               if dfs(nextNode):
                return True 
            visited[c] = False

            ret.append(c) #after all dependencies are done  this is the topological part 
        for c in graph: #topological sort requires that you run it on all nodes since graph doesnt need to be connected
            if dfs(c):
                return "" #invalid due to loop 
        ret.reverse()
        return "".join(ret)
           