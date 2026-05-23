class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L_pointer = 0
        for R_pointer in range(len(numbers)-1,0,-1): #negative for loop for R pointer 
            L_pointer = 0
            while L_pointer < R_pointer:
                if numbers[L_pointer] + numbers[R_pointer] == target:
                    return [L_pointer + 1, R_pointer + 1]
                else:
                    L_pointer += 1

        