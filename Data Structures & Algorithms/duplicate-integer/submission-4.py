class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for value in nums:
            if value in sett:
                return True
            sett.add(value)
        return False
         