import heapq
from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Step 1: sort by start time
        intervals.sort(key=lambda x: x.start)

        # Step 2: initialize a min-heap with the end time of the first meeting
        heap = [intervals[0].end]

        # Step 3: process remaining meetings
        for i in range(1, len(intervals)):
            # if the earliest meeting ends before the current one starts, re-use that room
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            # allocate the current meeting (new or reused room)
            heapq.heappush(heap, intervals[i].end)

        # heap size = min number of rooms required
        return len(heap)
