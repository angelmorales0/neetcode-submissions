class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0, len(height)-1
        ret=0
        maxRight = height[r]
        maxLeft = height[l]
        #calculate max from current spot, it is min (max right bound, max leftbound) -cur
        #let current index move when a new min is found to  nbe the current bound 

        while l<r:
            if maxLeft<= maxRight:
                l+=1
                maxLeft = max(maxLeft,height[l])
                water = maxLeft-height[l]
            else:
                r-=1
                maxRight = max(maxRight,height[r])
                water = maxRight-height[r]
            print(l,r,water,ret)
            ret +=water
        return ret