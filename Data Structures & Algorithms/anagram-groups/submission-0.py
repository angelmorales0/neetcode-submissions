class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        current_word = []
        for index in range (len(strs)):
            for letter in strs[index]:
                current_word.append(letter)
            #now current_word has all letters
            current_word.sort()
            if tuple(current_word) not in hash_map:
                hash_map[tuple(current_word)] = []
            hash_map[tuple(current_word)].append(strs[index])
            current_word.clear()
        return hash_map.values()
