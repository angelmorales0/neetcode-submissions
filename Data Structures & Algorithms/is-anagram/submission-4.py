class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = {}
        w2 = {}

        for ltr in s:
            w1[ltr] = w1.get(ltr,0) + 1
        for ltr in t:
            w2[ltr] = w2.get(ltr,0) + 1
        if w1 == w2:
            return True
        return False