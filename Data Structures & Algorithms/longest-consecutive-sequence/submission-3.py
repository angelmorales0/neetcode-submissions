class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lenMap = set()
        count = 0
        ret = 0
        for num in nums:
            lenMap.add(num)
        
        for val in lenMap:
            if val-1 not in lenMap:
                while val in lenMap:
                    val+=1
                    count+=1
                    ret = max(ret,count)
                count = 0
        return ret
       