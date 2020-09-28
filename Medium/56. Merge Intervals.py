class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]

        for i, pair in enumerate(intervals[1:]):
            x, y = pair
            if x <= ans[-1][1]:
                x1, y1 = ans[-1]
                ans[-1] = [min(x, x1), max(y, y1)]
            else:
                ans += [x, y],

        return ans


            
