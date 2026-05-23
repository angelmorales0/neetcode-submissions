class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted array so we can use binary search using L and R pointers
        L_point=0
        R_point = len(nums)-1 # last index

        while L_point <= R_point:
          middle_index = int((L_point + R_point)/2)

          if nums[int(middle_index)] > target:
            # greater than target so search left 
             R_point = middle_index -1
          elif nums[int(middle_index)] < target:
            # less than target so search right
              L_point = middle_index +1
          else:
            return middle_index
        return -1

