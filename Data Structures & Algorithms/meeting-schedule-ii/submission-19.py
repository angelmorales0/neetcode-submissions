"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        if not intervals:
            return 0
        ret = [intervals[0].end] 
        # Initalizes our Heap to only contain END times since that is all we care about

        for i in range(1,len(intervals)):
            if intervals[i].start >= ret[0]: #this means that the meeing time has ended 
                heapq.heappop(ret)
            heapq.heappush(ret, intervals[i].end)

        return len(ret)
        