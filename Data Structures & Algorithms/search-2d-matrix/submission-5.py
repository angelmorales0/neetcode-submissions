class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left= 0
        right = len(matrix[0]) - 1
        row= 0
        while row < len(matrix):

            if matrix [row][right] < target: # increment
                row += 1
            elif matrix [row][right] > target:

                while left <= right:
                    m = (left + right) // 2 
                    if matrix[row][m] > target: # go left:
                        right = m -1 
                    elif matrix[row][m] < target: 
                        left = m+1
                    else :
                        return True 

                return False  
            elif matrix [row][right] == target:
                return True

           
        return False
            