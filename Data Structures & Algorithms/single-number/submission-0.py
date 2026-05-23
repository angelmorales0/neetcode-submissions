class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        og = 0
        for num in nums:
            og = num ^ og
        return og
            
        