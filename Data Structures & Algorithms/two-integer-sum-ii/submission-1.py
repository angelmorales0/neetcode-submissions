class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index 1 must be less than index 2, return it one indexed, and the nums add up to target 
        #array is sorted 
        l=0
        r= len(numbers)-1

        while l<r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l +=1
            else:
                return [l+1,r+1]