class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyds algo !!!
        slow = 0
        fast = 0
        #let pointer point to index
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        
        return nums[slow]