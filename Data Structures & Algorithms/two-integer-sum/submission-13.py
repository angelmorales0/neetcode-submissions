class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberToIndex = {} #value:index
        for i in range(len(nums)):
            currentNumber = nums[i]
            leftOver = target -  currentNumber
            if leftOver in numberToIndex:
                return [numberToIndex[leftOver],i]
            numberToIndex[currentNumber] = i
            