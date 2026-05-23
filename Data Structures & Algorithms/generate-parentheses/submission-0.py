class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #at each step you have 2 options, open and close or just open and close later 
        ret = []    

        #implement a back track algo to add and remove this bitch on purpose 

       
        def dfs(p,o, curr): #curr = string 
            if p > n:
                return
            if p == n:
                if o == 0:
                    if curr not in ret:

                        ret.append(curr)
                    return 
                else:
                    while o > 0:
                        curr += (")")
                        o -=1
                    if curr not in ret:
                        ret.append(curr)
                    return

            dfs (p+1, o, curr + ("()"))
            dfs (p+1, o+1, curr + ("("))

            if o > 0:
              
                dfs (p,o-1, curr + (")"))

        dfs(0,0,"")
        return ret