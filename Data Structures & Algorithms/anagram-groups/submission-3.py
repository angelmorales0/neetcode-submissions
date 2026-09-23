class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Input = an array of strings, 
        Goal is to grpup all anagrams together 
        and returnout the output in group 

        BF = take one and compare it to all otehrs  eveyr time O(n^2)

        Anagram = character count is the same but order is different not a palindrome 
        """

        #make it a hashmap? for each item (o(N)) * str length 
        #then from there erge hashmaps with same values. key = word value = count?


        ret = defaultdict(list)

        for word in strs:
            letterCounts = Counter(word)
            sorted_by_key = {k: letterCounts[k] for k in sorted(letterCounts)} # o(1) because it is only constant letters?
            ret[tuple(sorted_by_key.items())].append(word)

        return list(ret.values())

        