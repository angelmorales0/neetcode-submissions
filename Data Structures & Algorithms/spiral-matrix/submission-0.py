class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        ret = []

        top = 0
        left = 0
        right = len(m[0])-1
        btm = len(m)-1

        while left <= right and top <= btm:
           
            for c in range(left,right+1):
               
                ret.append(m[top][c])  
            top +=1
            if top <= btm:

                for r in range(top,btm+1):
                    ret.append(m[r][right])
                right -=1

            if left <= right and top <= btm:

                for l in range (right,left-1,-1):
                    
                    ret.append(m[btm][l])
                btm-=1

            if top <= btm and left <= right:
                for t in range(btm,top-1,-1):
                    print(left)
                    ret.append(m[t][left])
                left +=1

            
        return ret