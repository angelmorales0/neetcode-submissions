class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumber = set()
        for num in nums:
            if num in seenNumber:
                return True
            seenNumber.add(num)
        return False
        