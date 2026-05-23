class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #width is 1 array is heigt 
        #return area of largest rectangle
        #hieght of rectangle = hieght of smallest thing in rectangle
        #rectanlge = something with diff width and height vals

        #bf = backtrack get all subsets and see if rectangle is greater than max area
        # o(n^2) include or not inclue are 2 options 
        ret = 0
        for i in range(len(heights)):
            minHeight = float('inf')
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                width = j-i+1
          
                ret = max(ret,width*minHeight)
        return ret

