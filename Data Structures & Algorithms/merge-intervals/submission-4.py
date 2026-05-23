#class Solution -> Def merge 
class Solution:
    def merge(self, intervals):
        intervals.sort() #sorts by starting val 
        i = 0
        #case 1 it overlaps because it starts after we startt and before we end 
        #case 2 it ovelaps because it ends anfter we start and before we end 
        while i < len(intervals)-1:
            is_overlapping = (intervals[i+1][0] <= intervals[i][1]) 
            
            if is_overlapping:
                intervals[i] = [min(intervals[i+1][0],intervals[i][0]), max(intervals[i+1][1],intervals[i][1])]
                intervals.pop(i+1)
                continue 
            i+=1
        return intervals
