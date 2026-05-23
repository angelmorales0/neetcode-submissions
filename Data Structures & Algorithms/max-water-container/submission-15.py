class Solution:
    def maxArea(self, heights: List[int]) -> int:
     # we are finding the max/min in a data set so the 2 pointers approach works best 
     L = 0
     R = len(heights)-1
     Current_max = 0
     while L < R:
        dist = R - L
        height = min(heights[L], heights[R])
        Current_max = max(Current_max, dist*height)
        #if Right height is smaller we should change that because it is the bottleneck
        #and only thing we can recieve benefits from changing
        if heights[L] > heights[R]: 
            R -= 1
        else:
            L += 1
     return Current_max