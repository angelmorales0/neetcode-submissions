class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key = lambda x: len(x))

        memo = {"": True} # map string left to true or false
        def dfs(string):
            if not string:
                return True

            for word in wordDict:
                if string.startswith(word):
                    next_word = string[len(word)::]
                    if next_word in memo:
                        return memo[next_word]
                    if dfs(next_word):
                        memo[string] = True
                        return True
            memo[string] = False
            return False
        return dfs(s)
                    
