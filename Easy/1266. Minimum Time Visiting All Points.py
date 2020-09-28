class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            x, y = points[i]
            x1, y1 = points[i - 1]
            ans += max(abs(x - x1), abs(y - y1))
        return ans 
