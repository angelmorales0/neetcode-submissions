"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = Interval(0,0)
        intervals.sort(key = lambda x: x.start)
        for meeting in intervals:
            if meeting.start < prev.end:
                return False
            prev = meeting
        return True

