class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # How do i model ts as a graph
        # Modeled as adjaencery list 

        #step 1 =  make a adjancery list hashmap where B is the key and A is the value 
        #that way we model our shit such that B contains an 'edge' learing to A 
        # (since b is reqed for a)

        #from there we can then loop throuhg our map 
        #and see that if the key is contained in the values of any value
        # then there is a loop so we return false #works for inifinite courses 

        #to make it work for num courses 

        #need to start at one with no inocming edges which is ??? And go through all options if 
        #we reach end then 

        preMap = {num: [] for num in range(numCourses)} #explained in rules!
        # it is asking if you can Take ALL courses, numCourses defines what all course is 
        for course, pre in prerequisites:           
            preMap[course].append(pre) #course -> prreq how do i ge courses w/ no dep?

        visited = set()

        def dfs(course):
            if course in visited:
                return False #loop
            if preMap[course] == []:
                return True #since we can take it 
            
            visited.add(course)
            for pre_course in preMap[course]:
                if not dfs(pre_course): return False #since it has a loop
            visited.remove(course)
            preMap[course] = [] #just so you dont have repeate work since if u 
            #get this far you know your sol is valid
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True




