class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0 ,len(nums) -1
        index = -1

        while L <= R:
            M = (L + R) // 2
            print(L)
            print(R)
            print(M)
            
            if nums[L] <= nums[R]:
                if nums[M] < target:
                    #it must be in right half 
                    L = M + 1
                elif nums[M] > target:
                    #it must be in left half
                    R = M-1
                else:
                    #index = target
                    index = M
                    return index 
            else:

                if nums[M] == target:
                    index = M
                    return index

                if nums[L] <= nums[M] and nums[L] < target:
                    # it must be below M 
                    #left half is sorted 
                    R = M -1
                elif nums[L] <= nums[M] and nums[L] >  target:
                    #target must be in other unsorted half 
                    L = M +1


                elif nums[M] <= nums[R] and nums[M] < target :
                    #it must be in right half 
                    #right half is sorted 
                    L = M + 1
                elif nums[M] <= nums[R] and target > nums[R]:
                    #it must be in the other unsorted half
                    R = M - 1
        return index