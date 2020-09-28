class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def go(x, y):
            i = 4
            i -= grid[x][y - 1] if y > 0 else 0
            i -= grid[x][y + 1] if y < len(grid[0]) - 1 else 0
            i -= grid[x - 1][y] if x > 0 else 0
            i -= grid[x + 1][y] if x < len(grid) - 1 else 0
            return i

        ans = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                ans += go(x, y) if grid[x][y] else 0

        return ans
