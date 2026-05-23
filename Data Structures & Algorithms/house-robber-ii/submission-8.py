class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
            print(arr)
            last = len(arr)
            maxmoney = 0
     
            for i in range(last-3, -1, -1):
                arr[i] = arr[i] + max(arr[i+2:])
        
            for num in arr:
                maxmoney = max(maxmoney, num)
            print(arr)
            return maxmoney
    
        if len(nums) <= 3:
            return max(nums)
        return max(helper(nums[1:].copy()), helper(nums[:-1].copy()))
        