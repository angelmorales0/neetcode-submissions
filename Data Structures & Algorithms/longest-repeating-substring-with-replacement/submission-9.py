class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      count_map = {}
      l_pointer = 0
      current_length = 0
      max_length = 0

      for r_pointer in range (len(s)):
        count_map[s[r_pointer]] = count_map.get(s[r_pointer], 0) + 1
        current_length = 1 + r_pointer - l_pointer
        while  k < current_length - max(count_map.values()) :
            count_map[s[l_pointer]] -= 1 #decrement count map 
            l_pointer += 1
            current_length = 1 + r_pointer - l_pointer
        max_length = max(max_length, current_length)
      return max_length 

        #grow the window
      #shrink the window until it is valid 
