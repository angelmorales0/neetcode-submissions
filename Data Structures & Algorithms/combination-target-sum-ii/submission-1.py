class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ret = []
        candidates.sort() # WHY DOES SORTING IT CHANGE IT 

        def backtrack(index):
            
            tot = 0
            for number in arr:
                tot += number

    

            if tot == target and arr not in ret:
                ret.append(arr.copy())
                return 
                
            if index >= len(candidates) or tot > target :
                return # base case
            
            if tot < target:
                #case where we DO include our number
                arr.append(candidates[index])
                backtrack(index + 1)
                arr.pop()
            
                #case where we dont include our current number 
              
                backtrack(index + 1)

            


        backtrack(0)
        return ret
        