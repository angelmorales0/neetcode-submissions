"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        maxCount = 0
        s = []
        e = []
        if not intervals:
            return 0

        for i in intervals:
    
            s.append(i.start)
            e.append(i.end)

        s.sort()
        e.sort()

        for i in range(len(s)):
            if e[0] <= s[i]:
                e.pop(0)
                count -= 1 #since we dont need the room 
            count += 1
            maxCount = max(maxCount, count)
            
            
       
        return maxCount 


        