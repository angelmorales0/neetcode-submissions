class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #2 approaches -> seen set which uses extra space or we
        # could use a more math approach since we know it decreases by one each time 

        # we can stop
        #approachs = layer by layer + recursion RO 
        #or and iterative which is where we give a bound number
        # and just iterate while bound can go up or down 

        bound = 0
        #leftBound = 0 top bound = bound #BOUND IS INCLUSIVE 
        #Btm bound = len(matrix)-1-bound
        #right bound = len(matrix[0]) -1 -bound

        #while left bound < right bound or top bound < btm bound #fir size 1 
            #go right to len(matrix[0]) -1 -bound
            #go down to len(matrix) -1 -bound
            #go left to bound (including)
            #increment bound
    #         go up to bound to not double count 
        ret = []
        while bound <= len(matrix[0]) - 1 - bound and bound <= len(matrix) - 1 - bound:
            far_right = len(matrix[0]) -1 -bound
            far_left = bound
            top = bound
            btm = len(matrix)-1-bound
            
            if bound < len(matrix):
                for c in range(bound, len(matrix[0]) -bound):
                    ret.append(matrix[bound][c])

            for r in range(bound+1, btm+1): #b+1 to not double count 3 
                ret.append(matrix[r][far_right])

            if top != btm :
                for c2 in range(far_right-1,far_left-1,-1):
                    ret.append(matrix[btm][c2])
            if far_right != far_left:    
                for r2 in range(btm-1,top,-1): #bound since we dont want t revist it exlcusiev"
                    ret.append(matrix[r2][far_left])
            bound +=1 

        if len(matrix[0]) -1 -bound == bound and bound == len(matrix)-1-bound:
            ret.append(matrix[bound][bound])
        return ret
