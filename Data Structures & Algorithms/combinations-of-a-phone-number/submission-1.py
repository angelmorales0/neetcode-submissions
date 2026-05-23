class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        cur =[""]
        mapp = {}
        mapp["2"] = ["a","b","c"]
        mapp["3"] = ["d","e","f"]
        mapp["4"] = ["g","h","i"]
        mapp["5"] = ["j","k","l"]
        mapp["6"] = ["m","n","o"]
        mapp["7"] = ["p", "q","r","s"]
        mapp["8"] = ["t","u","v"]
        mapp["9"] = ["w","x", "y","z"]

        def backtrack(index):
            if index >= len(digits):
                ret.append(cur[0])
                return 

            for letter in mapp[digits[index]]:
                cur[0] += letter
                backtrack(index+1)
                cur[0] = cur[0][:len(cur[0]) -1:]


        backtrack(0)
        if ret == [""]:
            return []
        return ret
        