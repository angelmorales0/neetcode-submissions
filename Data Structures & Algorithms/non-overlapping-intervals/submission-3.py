class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        #sorts by the start time 

        #remove the one with a bigger range gredily 
        ret = []
        count = 0
        i=0

        while i < len(intervals)-1:
            is_overlapping = (intervals[i+1][0] < intervals[i][1])
            #remove the bigger interval  and restart, you can only progress when you are no longer overlapping 
            #here I think we can greedily remove it and itll be fine, proof tho? IDK 
            if is_overlapping:
                if (intervals[i+1][1]) <= (intervals[i][1]): #if next is >= remove next else romeve curer
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
                count +=1
                continue
            else:
                i+=1
        return count