class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range (len(nums)+1):
            total += i
        return total - sum(nums)
        """
        input is a list of integers from 0 to n return the one that is missing 

        time,    space 
        o(nlogn),    o(1)
        o(n),    o(n)
        """

        

