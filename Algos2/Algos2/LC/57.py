# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        

        output = []

        yetToAppend = True

        i = 0
        n = len(intervals)
        temp = Interval(newInterval.start, newInterval.end)

        while i < n:


            if newInterval.start > intervals[i].end:
                # new interval will com after i
                output.append(intervals[i])

            elif (intervals[i].end <= newInterval.end and intervals[i].end >= newInterval.start) or \
                (intervals[i].start >= newInterval.start and intervals[i].start <= newInterval.end) or \
                (intervals[i].start <= newInterval.start and intervals[i].end >= newInterval.end):
                temp.start = min(temp.start, intervals[i].start)
                temp.end = max(temp.end, intervals[i].end)
                yetToAppend = True
            elif newInterval.end <= intervals[i].start:
                if yetToAppend:
                    output.append(temp)
                    yetToAppend = False
                output.append(intervals[i])


            i += 1




        if yetToAppend:
            output.append(temp)



        return output




