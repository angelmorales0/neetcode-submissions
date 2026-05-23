class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0,len(nums) -1
        M =  int((L + R )/2)

        while L <= R:
            if nums[M] == target:
                return M
            elif nums[M] > target:
                R = M -1
                M =  int((L + R )/2)
            elif nums[M] < target:   
                L = M + 1
                M =  int((L + R )/2)
        return -1
        