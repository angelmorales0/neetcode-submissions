class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = defaultdict(list)
       

        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char) - ord('a')] +=1
            ret[tuple(key)].append(word)
            
        return list(ret.values())

