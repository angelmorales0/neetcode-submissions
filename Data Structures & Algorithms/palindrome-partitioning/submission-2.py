import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        For A in range b 
        Maintaing this property is chopped almost t hink it would be better to gen all substrings 
        then check if its a pali then retuirn 

        a  -> aa
        "" a 
        """
        palindromes = []
        def dfs(i, currentString, currentPalis):
            if currentString and currentString == currentString[::-1]:
                
                currentPalis.append(currentString)
                dfs(i+1, "", currentPalis) #skip case 
                if i < len(s):
                    dfs(i+1,s[i], currentPalis) # include case
                currentPalis.pop()
           
            

            if i >= len(s):
                count = 0
                for word in currentPalis:
                    for char in word:
                        count +=1
                if count == len(s):
                    palindromes.append(copy.deepcopy(currentPalis))
                return

           
            dfs(i+1,currentString+ s[i], currentPalis)
            dfs(i+1 ,currentString, currentPalis)
        dfs(0, "",[])
    
        return palindromes
