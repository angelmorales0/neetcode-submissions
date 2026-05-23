class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for number in nums:
            my_set.add(number)
        if (len(my_set) == len(nums)):
            return False
        else:
            return True
           
