from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def longer(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + longer(i+1,j+1)# 1+ since char matcehs
            else:
                return max(longer(i+1,j), longer(i,j+1))
        return longer(0,0)

            