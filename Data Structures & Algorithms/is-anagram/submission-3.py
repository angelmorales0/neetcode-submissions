class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp1 ={}
        mapp2 = {}
        if len(s) != len(t):
            return False

        for i in range (len(s)):
            mapp1[s[i]] = mapp1.get(s[i],0) + 1
            mapp2[t[i]] = mapp2.get(t[i],0) + 1
        if mapp1 == mapp2:
            return True
        return False
        