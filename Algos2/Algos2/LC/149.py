from collections import defaultdict


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        lineCount = defaultdict(lambda : defaultdict(int))

        n = len(points)

        if n == 0:
            return 0
        if n == 1:
            return 1
            
        same = defaultdict(int)

        for i in range(n):
            for j in range(i+1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    # don't compare the same points
                    same[i] += 1
                    continue                

                if (points[i].x - points[j].x) == 0:
                    slope = 0
                else:
                    slope = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
                intercept = points[i].y - points[i].x * slope

                if lineCount[i][(slope, intercept)] == 0:
                    lineCount[i][(slope, intercept)] = 1
                else:
                    lineCount[i][(slope, intercept)] += 1

        count = 0


        for i in range(n):
            m = 0
            
            for v in lineCount[i]:                
                m = max(m, lineCount[i][v])

            # add the point and all duplicates
            count = max(count, m+same[i]+1)



        return count







if __name__ == '__main__':
    s = Solution()
    s.maxPoints([Point(1,1), Point(1,1), Point(2,3)])
