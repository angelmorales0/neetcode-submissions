class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        for L in range(len(heights)-1):
            if L > 0 and heights[L] < heights[L-1]:
                continue
            for R in range(len(heights)-1, L, -1):
                if R-1 > L and heights[R-1] < heights[R-1]:
                    continue
                
                dist = R - L 
                height = min(heights[L], heights[R])
                area = dist*height
                current_max = max(current_max, area)
        return current_max