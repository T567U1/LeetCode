class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        y_diff_1 = points[1][1] - points[0][1]
        x_diff_1 = points[1][0] - points[0][0]

        y_diff_2 = points[2][1] - points[1][1]
        x_diff_2 = points[2][0] - points[1][0]

        return x_diff_1 * y_diff_2 != x_diff_2 * y_diff_1
