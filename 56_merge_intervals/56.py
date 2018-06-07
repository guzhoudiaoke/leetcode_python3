# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "[%2d, %2d]" % (self.start, self.end)

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key = lambda x : x.start)
        ans = [intervals[0]]
        
        for interval in intervals[1: ]:
            if ans[-1].end < interval.start:
                ans.append(interval)
            elif ans[-1].end < interval.end:
                ans[-1].end = interval.end

        return ans
        
sol = Solution()

def makeIntervals(intervals):
    ans = []
    for interval in intervals:
        ans.append(Interval(interval[0], interval[1]))
    return ans

def printIntervals(intervals):
    for interval in intervals:
        print(interval, end=', ')
    print()

intervals = makeIntervals([[1,3], [8,10], [2,6], [15,18]])
printIntervals(sol.merge(intervals))

intervals = makeIntervals([[1,4], [4,5]])
printIntervals(sol.merge(intervals))
