class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #have a hashmap showing deps -> can have multi so itll be an array 
        graph = {c:set() for w in words for c in w} #gets us a set with every cahr 

        for i in range(len(words)-1):
            w1 = words[i] 
            w2 = words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #not a valid string input from instructions 
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j]) # since we KNOW that w2 comes AFTER w1
                    break
        visited = {}
        ret = []

        def dfs(c): #this is the topoligcal sort 
            if c in visited:
                return visited[c] # if this returns true then there is a loop which makes our graph ordering invalid== return ""
            visited[c] = True

            for neighbor in graph[c]:
                if dfs(neighbor):
                    return True #Loop 
            visited[c] = False
            ret.append(c)

        for c in graph:
            if dfs(c):
                return ""

        ret.reverse()
        return "".join(ret)