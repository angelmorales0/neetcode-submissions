class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        for L in range(len(heights)-1):
            for R in range(L+1, len(heights), 1):
                dist = R - L 
                height = min(heights[L], heights[R])
                area = dist*height
                current_max = max(current_max, area)
        return current_max