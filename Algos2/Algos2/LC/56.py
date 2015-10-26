# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        

        n = len(intervals)

        output = []
        
        intervals = sorted(intervals, key=lambda x: x.start)

        if n == 0:
            return output

        start = intervals[0].start
        end = intervals[0].end

        for i in range(1,n):
            if intervals[i].start > end:
                output.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end 

            else:
                end = max(end, intervals[i].end)


        output.append(Interval(start, end))

        return output

