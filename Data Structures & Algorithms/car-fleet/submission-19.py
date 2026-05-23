class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        lit = []
        stack= []
        for i in range (len(speed)):
            lit.append([position[i],speed[i]])
        lit.sort(reverse=True)
        for car in lit:
            time = ( target - car[0])/ car[1]
            print(time)
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time) 

        return len(stack)