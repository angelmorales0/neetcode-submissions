class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReqs = {course: [] for course in range(numCourses)} #maps courses to its pre-reqs
        
        for course, pre in prerequisites:
            preReqs[course].append(pre)

        visited = set() #for loop detection
        def dfs(course):
            if preReqs[course] == []:
                return True 
            if course in visited: 
                return False 
            visited.add(course)
            for pre in preReqs[course]:
                if not dfs(pre): # WE have a cycle so just return false 
                    return False 
            visited.remove(course)
            preReqs[course] = []
            return True
        for course, pre in prerequisites:
            if not dfs(course): return False
        return True
        
            