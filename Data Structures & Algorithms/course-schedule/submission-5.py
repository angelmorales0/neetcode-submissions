class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False #CYCLE DETECETED
            visited.add(crs)
            if crs in preMap:
                for prereq in preMap[crs]:
                    if not dfs(prereq):
                        return False
            visited.remove(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True