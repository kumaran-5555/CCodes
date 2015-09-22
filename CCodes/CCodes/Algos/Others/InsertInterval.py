#!/usr/bin/python3
__author__ = 'kumaran'



class Solution():
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        # intervals are non overlapping

        l = len(intervals)
        start = None
        end = None
        output = []

        if not l:
            output.append(newInterval)
            return output

        i = 0
        foundStart = False
        done = False

        # skip the intervals which falls before newInterval's start
        while i < l and intervals[i].end < newInterval.start:
            output.append(intervals[i])
            i += 1

        # all intervals are before newInterval
        if i == l:
            output.append(newInterval)
            return output


        while i < l:




            if not foundStart:
                if intervals[i].start > newInterval.start:
                    start = newInterval.start
                elif intervals[i].start <= newInterval.start:
                    start = intervals[i].start
                foundStart = True
                continue

            if foundStart:
                if newInterval.end < intervals[i].end and newInterval.end < intervals[i].start:
                    end = newInterval.end
                    break
                elif newInterval.end >= intervals[i].start and newInterval.end <= intervals[i].end:
                    end = intervals[i].end
                    i += 1
                    break
                elif newInterval.end > intervals[i].end:
                    i += 1
                    continue


        if start is not None and end is None:
            end = newInterval.end



        output.append(Interval(start, end))

        while i < l:
            output.append(intervals[i])
            i += 1

        return  output







if __name__ == '__main__':
    s = Solution()
    
