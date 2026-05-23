class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                print(nums[slow])
                break #we are at point of intersection 
        #run floyds algo to find the start of the list?

        new_slow = 0
       

        while new_slow != slow:
            print(slow)
            new_slow = nums[new_slow]
            slow = nums[slow]
        return new_slow