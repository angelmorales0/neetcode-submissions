class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #return max water we can stow type shit 
        #choose from any 2 means two pointers probably

        #Max water a container can store is ??


        #iterate through it end to end and move the one with the most reward

        #check both and see what has more reward?


        l = 0
        r = len(heights)-1

        ret = 0
        while l < r:
            height = min(heights[l],heights[r]) * (r-l)
            ret = max(ret,height)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return ret
            #Need to find a way to move pointer rn approach is greedy but 

            #IF R. > L MOVE L BECAUSE L IS OUR BOTTLENECK
            #5 1 30 6 3 30 5

