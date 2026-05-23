class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        current_max_RH = 0
        current_max_LH = 0

        for L in range(len(heights)-1):
            if current_max_LH > heights[L]:
                continue
            current_max_LH = max(current_max_LH,heights[L])

            for R in range(len(heights)-1, L, -1):
                if current_max_RH > heights[R]:
                    continue
                dist = R - L 
                height = min(heights[L], heights[R])
                current_max_RH = max(current_max_RH,height)
                area = dist*height
                current_max = max(current_max, area)
        return current_max