class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret= []

        for i in range(len(intervals)):
            if newInterval[1] < intervals [i][0]: #if our new end is < our current start
                ret.append(newInterval)
                return ret + intervals[i:]
            elif newInterval[0] > intervals[i][1]:  #new interval start is AFTER our end 
                ret.append(intervals[i])
            else: #build up the merged new interval 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] #merge
        ret.append(newInterval)
        return ret
