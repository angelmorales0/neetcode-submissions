class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursemap = {}
        arr = []
        q = deque()
        visited = set()
        cycle = set()

        for course, prereq in prerequisites:
            if course not in coursemap:
                coursemap[course] =[]
            coursemap[course].append(prereq)
        print(coursemap)

        def dfs(course):
            if course in cycle:
                return False #CYCLE PRESENT 
            if course in visited:
                return True # we already visited this node 
            
            cycle.add(course)
            if course in coursemap:
                for pre in coursemap[course]:
                    if not dfs(pre): #CYCLE 
                        return False
            cycle.remove(course)
            visited.add(course)
            arr.append(course)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []
        return arr

            

          
                

            
        