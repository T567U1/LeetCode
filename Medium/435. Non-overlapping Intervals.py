class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        ans = 0
        end_ = intervals[0][1]
        for i, interval in enumerate(intervals[1:]):
            if interval[0] < end_:
               ans += 1
            else:
                end_ = interval[1]
