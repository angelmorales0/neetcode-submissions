class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        cur = []
        n = len(s)
        
        def backtrack(index):
            if index >= n:
                ret.append(cur.copy())
                return 
             
            for fut in range(index,n):
                if s[index:fut+1] == s[index:fut+1][::-1]:
                    cur.append(s[index:fut+1])
                    backtrack(fut+1)
                    cur.pop()
            return

            
        backtrack(0)
    
        return ret

