class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursemap = {}
        arr = []
        visited = set()
        cycle = set()

        for course, prereq in prerequisites:
            if course not in coursemap:
                coursemap[course] =[]
            coursemap[course].append(prereq) # maps all courses to their dependencies 

        
        def dfs(course):
            if course in visited:
                return True #not cycle just repeated work 

            if course in cycle:
                return False 

            cycle.add(course)
            if course in coursemap: #if we have dependencies
                for pre in coursemap[course]:
                    if not dfs(pre):
                        return False
                    
            cycle.remove(course)
            visited.add(course)
            arr.append(course)
            return True #since we want false ONLY IF CYCLE IS PRESENT



        for i in range(numCourses):
            if not dfs(i):
                return []
        return arr
            
                

            
        