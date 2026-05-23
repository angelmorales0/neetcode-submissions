class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        while L != R:
            M = 1 + ((L + R)// 2)
            if matrix[M][0] > target: # we know it isnt aove the middle index so we let L = M+1
                R = M-1 
            if matrix[M][0] < target: # we know it isnt above the middle index so we let L = M+1
                L= M 
            if matrix[M][0] == target:
                return True

        L_I, R_I = 0, len(matrix[L])-1
        while L_I <= R_I:
            M_I = (L_I + R_I) // 2
            if matrix[L][M_I] < target:
                L_I = M_I + 1
            if matrix[L][M_I] > target:
                R_I = M_I - 1
            if matrix[L][M_I] == target:
                return True
        return False
                    