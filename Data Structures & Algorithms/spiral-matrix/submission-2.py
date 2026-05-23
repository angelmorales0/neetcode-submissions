class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #2 approaches -> seen set which uses extra space or we
        # could use a more math approach since we know it decreases by one each time 

        # we can stop
        #approachs = layer by layer + recursion RO 
        #or and iterative which is where we give a bound number
        # and just iterate while bound can go up or down 

        bound = 0 
        rows = len(matrix)
        cols = len(matrix[0])
        ret = []
        while bound < (rows - bound) and bound < (cols - bound):
            for c in range(bound, len(matrix[0]) - bound): # GO RIGHT

                ret.append(matrix[bound][c]) 
            for r in range(bound+1, len(matrix)- bound): # GO DOWN 
                ret.append(matrix[r][c])
            if rows - 1 - bound > bound:
                for c in range(cols - 2 - bound, bound - 1, -1):
                    ret.append(matrix[rows - 1 - bound][c])

            if cols - 1 - bound > bound:
                for r in range(rows - 2 - bound, bound, -1):
                    ret.append(matrix[r][bound])
            bound +=1

        if  len(matrix)-1 - bound == bound and len(matrix[0]) -1 - bound == bound:
            ret.append(matrix[bound][bound])
        return ret
            #go up to bound
