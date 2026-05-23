class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} 
        current_word_characters = []
        for index in range (len(strs)):
            for character in strs[index]:
                current_word_characters.append(character) # we add a character to our character list
            current_word_characters.sort()
            if tuple(current_word_characters) not in hash_map:# create new value append value\
                hash_map[tuple(current_word_characters)] = [strs[index]]
            else:
                hash_map[tuple(current_word_characters)].append(strs[index])
            current_word_characters.clear()
        return hash_map.values()
