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
        ret = []
        print([(i.start, i.end) for i in intervals])


        #as min conlicts but each conflict is a day?

        #curr idea = have a list full of diff days and map each interval to a day 
        #see if a conflict arises within all meeting intervals
        # if it does append that interval as a new list to the meeting 
        #if it doesnt append it to the day 

        for current_meeting in intervals:
            scheduled = False

            for scheduled_meetings_list in ret:   #add it if found with no conflict 
                scheduled_meeting = scheduled_meetings_list[-1]
                if current_meeting.start < scheduled_meeting.end:
                    continue
                else:
                    scheduled_meetings_list.append(current_meeting)
                    scheduled = True
                    break
            if not scheduled:
                ret.append([current_meeting])
        return len(ret)
        